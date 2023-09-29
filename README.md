# nlp-app

# Code Explanation and assumptions :
1. The file data-processing.ipynb contains the code which is used to preprocess and merge the three initial datasets ("Category","brand_category","offer retailer") to "final.csv" which will be used for further analysis .
2. Renamed the brand_belongs_to_category to product_category as both conveyed the same information.
3. Dropped the category_id from the categories.
4. Performed an outer merge for all the three datsets and save the resulting data as "final.csv" .

5. 

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
