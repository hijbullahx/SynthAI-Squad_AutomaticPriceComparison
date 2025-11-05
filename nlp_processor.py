import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

# Load the small English SpaCy model
# We load it *once* here to be efficient.
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("Model 'en_core_web_sm' not found. Please run:")
    print("python -m spacy download en_core_web_sm")
    # In a real app, you might exit or handle this more gracefully
    nlp = None

if nlp:
    # Add the 'spacytextblob' component to the NLP pipeline.
    # This "teaches" SpaCy how to understand sentiment.
    # We use 'last=True' to add it at the end of the pipeline.
    nlp.add_pipe('spacytextblob', last=True)

def analyze_sentiment(review_text):
    """
    Analyzes the sentiment of a given text.

    Returns a label: "Positive", "Neutral", or "Negative".
    """
    if not nlp or not review_text:
        return "N/A" # Return "Not Available" if model failed or text is empty

    # Process the text with the full SpaCy pipeline
    doc = nlp(review_text)

    # Get the polarity score from TextBlob
    # Polarity is a float between -1.0 (Very Negative) and 1.0 (Very Positive)
    polarity = doc._.blob.polarity

    # Convert the number score into a simple text label
    if polarity > 0.2:
        return "Positive"
    elif polarity < -0.2:
        return "Negative"
    else:
        return "Neutral"

# --- Test the function (you can run 'python nlp_processor.py' to test) ---
if __name__ == "__main__":
    test_text_1 = "Amazing service! My apartment is spotless. Very professional and on time."
    test_text_2 = "Average service. They missed a few spots and I had to call them back."

    print(f"'{test_text_1}' --> {analyze_sentiment(test_text_1)}")
    print(f"'{test_text_2}' --> {analyze_sentiment(test_text_2)}")