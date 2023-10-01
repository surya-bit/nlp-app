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

6. The main file "app.jsx" which does the functionality of front end is found in the client/src directory .
    1. Import various dependencies and assets, including React hooks (useState, useEffect), icons from react-icons, Axios for making HTTP requests, and a Vite logo image.
    2. Do the state management.
    3. The useEffect hook is triggered when the query state changes.If the query is not empty, it sends a POST request to the specified API endpoint with the search 
       parameters and updates the results state with the response data.
    4. UI rendering and CSS styling is done accordingly.
    5. The server communication component communicates with a server located at http://127.0.0.1:5000. It sends a POST request to this server when the user performs a 
       search.

# Installation libraries
There is requirements file in client which has all the libraries needed to run the code.
python3, node , npm , flask , pip , tensorflow , pytorch , transformers , pandas , sklearn.metrics.pairwise .

# Instructions on how to run the tool locally
1. This repo cotains two folders : client and server .
2. Move to the client folder and run the command : npm i (Installs all the packages)
3. Open a new terminal and move into the server folder : run python server.py
4. This will start server on port 5000 . (http://localhost:5000)

5. Move to the client folder again and run the command : npm run dev (Starts client side program)
6. Navigate to http://localhost:5173
7. By default the table prints No offers found and no similartiy score . 
8. Select one of the options and type the keyword you want to search in the search bar and click enter.
9. The output will be in a table format containing relevant offer and similarity score .

#Output 
1. ![image](https://github.com/surya-bit/nlp-app/assets/61753483/ca0f5a51-db49-418d-941d-c44d3ab4b603)
2. ![image](https://github.com/surya-bit/nlp-app/assets/61753483/808e7b7a-ab83-4dcf-b5d1-06f1d8e02a0e)

# Future Work :
1. This model can be made more effective by using ElasticNet Search instead of string matching and comparing.
2. THe interface could be made more interactive by including a drop down menu in the search tab.
