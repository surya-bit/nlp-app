# nlp-app

# Code Explanation and assumptions :
1. The file data-processing.ipynb contains the code which is used to preprocess and merge the three initial datasets ("Category","brand_category","offer retailer") to "final.csv" which will be used for further analysis .
2. Renamed the brand_belongs_to_category to product_category as both conveyed the same information.
3. Dropped the category_id from the categories.
4. Performed an outer merge on all the three datasets and dropped the missing values. 

5. In the server directory is the server.py file which does the following functionalities :
   1. Import all the necessary libraries needed.The installation libraries are given below.
   2. Initialize the flask application.
   3. Load the BERT model and tokenizer.
   4. Define a function compute_cosine_similarity to calculate cosine similarity between a query and a set of text embeddings.
   5. Define the search functions . These functions filter the dataset based on the user's input for category, brand, or retailer, respectively.
   6. Defines a function compute_similarity that takes a query and a list of texts as input. It tokenizes the query and texts, obtains BERT embeddings for them, and then 
      calculates cosine similarity scores between the query and each text.
   7. Define a single POST route ('/') to handle incoming search requests. The search function is executed when a POST request is made to the root endpoint ('/').
   8. Depending on the selected search option, it calls one of the three search functions ('search_by_category', 'search_by_brand', or 'search_by_retailer') to filter the 
      dataset based on the user's input.
   9. If relevant offers are found in the dataset, it calculates similarity scores between the user's input and the offers using the compute_similarity function. It then 
      adds these scores to the DataFrame, sorts the offers by similarity score in descending order, and converts the relevant offers and their similarity scores to JSON.
   10. The application is run when the script is executed. 

# Installation libraries
python3, node , npm , flask , pip , tensorflow , pytorch , transformers , pandas , sklearn.metrics.pairwise .

# Instructions on how to run the tool locally
1. This repo cotains two folders : client and server .
2. Open a new terminal and cd into the server folder : python server.py
3. This will start server on port 5000 . (http://localhost:5000)

4. cd into the client folder and run the command : npm i (Installs all the packages)
   npm run dev (Starts client side program)
5. Navigate to http://localhost:5173
6. By default the table prints No offers found and no similartiy score . 
7. Select one of the options and type the keyword you want to search in the search bar and click enter.
8. The output will be in a table format containing relevant offer and similarity score .
