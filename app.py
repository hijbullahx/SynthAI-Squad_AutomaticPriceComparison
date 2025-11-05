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

    # --- STEP 3: SHOW DATA (Temporarily) ---
    # Let's print the DataFrame to our terminal to see it.
    print("--- Scraped Data as DataFrame ---")
    print(df)
    print("---------------------------------")

    # And for the browser, we'll return the DataFrame as an HTML table.
    # This is just for testing! We'll make a beautiful results
    # page in the next phase.
    return f"""
    <html>
        <head>
            <title>Results</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
        </head>
        <body class="container p-5">
            <h1 class="mb-4">Found {len(df)} services for: {service_type}</h1>
            <p>Data returned from our scraper with AI sentiment analysis:</p>
            {df.to_html(classes='table table-striped table-hover', index=False)}
            <br>
            <a href="/" class="btn btn-primary">Try a New Search</a>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)