This project has 2 parts
1- A crop recomender that uses datasets from kaggle to recommend crops based on soil parameters
2- A web page that uses the trained model to recomend crops based on users form input and give fertizer recomendation (rule based), python flask module is used for this website

Key files / Folders:

1. The data_ai folder has:
    source data (Crop_recommendation.csv)
    range values for soil parameters of every crop (extracted from source data) soil_param_thresholds.csv
    trained model for predicting crops as a pickle file  (LogisticRegression.pkl)

2. ai_train.py   contains the AI code for creating a trained model

3. Back_end.py   code to extract soil parameter ranges for the rule based system - stored in a csv file  (soil_param_thresholds.csv)

4. main.py   The web page to take user input and to give out recomendations

5. The templates folder contains html files for the web page