from flask import Flask, request, jsonify
import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModel
from flask_cors import CORS
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
# Load your dataset with missing values
df = pd.read_csv('final.csv')

# Load the pre-trained BERT model and tokenizer
model_name = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# Define a function to compute cosine similarity
def compute_cosine_similarity(query_embedding, text_embeddings):
    dot_product = torch.sum(query_embedding * text_embeddings, dim=-1)
    query_norm = torch.norm(query_embedding, dim=-1)
    text_norm = torch.norm(text_embeddings, dim=-1)
    cosine_similarities = dot_product / (query_norm * text_norm)
    return cosine_similarities

def search_by_category(category):
    # Filter the dataset for rows with a matching category (assuming the column is "PRODUCT_CATEGORY")
    relevant_offers = df[df["PRODUCT_CATEGORY"].str.lower() == category.lower()]

    return relevant_offers

def search_by_brand(brand):
    # Filter the dataset for rows with a matching brand (assuming the column is "BRAND")
    relevant_offers = df[df["BRAND"].str.lower() == brand.lower()]

    return relevant_offers

def search_by_retailer(retailer):
    # Filter the dataset for rows with a matching retailer (assuming the column is "RETAILER")
    relevant_offers = df[df["RETAILER"].str.lower() == retailer.lower()]

    return relevant_offers

def compute_similarity(query, texts):
    # Tokenize the query and texts
    query_tokens = tokenizer(query, padding=True, truncation=True, return_tensors="pt")
    text_tokens = tokenizer(texts, padding=True, truncation=True, return_tensors="pt")

    # Get BERT embeddings for the query and texts
    with torch.no_grad():
        query_embedding = model(**query_tokens).last_hidden_state[:, 0, :]  # Take the [CLS] token embedding
        text_embeddings = model(**text_tokens).last_hidden_state[:, 0, :]  # Take the [CLS] token embedding

    # Calculate cosine similarity between the query and texts
    cosine_similarities = compute_cosine_similarity(query_embedding, text_embeddings)

    return cosine_similarities

@app.route('/', methods=['POST'])
def search():

    data = request.get_json()
    if 'key1' not in data:
            raise ValueError("Missing 'key1' in the request data")
    user_input = data['key1']
    option = data['key2']
    # Example: Search by category (assuming you have a function called search_by_category)
    if option == 'category':
        relevant_offers = search_by_category(user_input)  # Extract the single user input
    
    if option == 'brand':
        relevant_offers = search_by_brand(user_input)  # Extract the single user input
    
    if option == 'retailer':
        relevant_offers = search_by_retailer(user_input)  # Extract the single user input

    if not relevant_offers.empty:
        # Calculate similarity scores for each offer
        similarity_scores = compute_similarity([user_input[0]] * len(relevant_offers), relevant_offers["OFFER"].tolist())

        # Convert the PyTorch tensor to a list
        similarity_scores = similarity_scores.tolist()

        # Add the similarity scores to the DataFrame
        relevant_offers["SIMILARITY_SCORE"] = similarity_scores

        # Sort the offers by similarity score (descending order)
        relevant_offers = relevant_offers.sort_values(by="SIMILARITY_SCORE", ascending=False)

        # Convert the relevant offers and their similarity scores to JSON
        result = relevant_offers[["OFFER", "SIMILARITY_SCORE"]].to_dict(orient='records')
        return jsonify(result)
    else:
        return jsonify({"message": "No relevant offers found."})

if __name__ == '__main__':
    app.run(debug=True)
