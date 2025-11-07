from flask import Flask, render_template, request
import pandas as pd                   
from scraper import get_service_data  
from nlp_processor import analyze_sentiment

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare():
    """
    Handles the data submitted from the form.
    """
    service_type = request.form.get('service_type')
    location = request.form.get('location')

    # --- STEP 1: GET DATA ---
    # Call our mock scraper function
    data_list = get_service_data(service_type, location)

    # What if the scraper returns nothing?
    if not data_list:
        # Handle case where no data is found (important for real scrapers)
        return "<h1>No data found for your search.</h1>"

    # --- STEP 2: STORE IN PANDAS DATAFRAME ---
    # Convert the list of dictionaries into a DataFrame (a table)
    df = pd.DataFrame(data_list)

    df['sentiment'] = df['review_summary'].apply(analyze_sentiment)

   # --- STEP 4: PREPARE DATA FOR TEMPLATE ---
    print("--- DataFrame with NLP Sentiment ---")
    print(df)
    print("------------------------------------")

    data_for_template = df.to_dict(orient='records')

    return render_template('results.html',
                       service_data=data_for_template,
                       service_type=service_type,
                       location=location)

if __name__ == '__main__':
    app.run(debug=True)