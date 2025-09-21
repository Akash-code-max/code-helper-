import requests
from flask import Flask, jsonify, abort

# Initialize the Flask app
app = Flask(__name__)

# --- IMPORTANT ---
# This dictionary maps a short name (like "GP3") to a Google Doc ID.
# Replace the placeholder value with your real Google Doc ID.
DOCS = {
    "GP3": "your_doc_id_here"  # <-- PASTE YOUR GOOGLE DOC ID HERE
}

@app.route('/get_code/<doc_name>')
def get_code(doc_name):
    """
    Fetches text content from a public Google Doc and returns it as JSON.
    """
    # Look up the doc ID from the dictionary using the name from the URL
    doc_id = DOCS.get(doc_name)

    # If the name isn't in our dictionary, return a 404 Not Found error
    if not doc_id:
        abort(404, description=f"Document '{doc_name}' not found.")

    # Construct the public export URL for the Google Doc
    url = f"https://docs.google.com/document/d/{_1rMygbu1llfsKIq2u5SHHNxRcIH7a0xYFDVp_AC-m66s}/export?format=txt"

    try:
        # Fetch the content from the URL
        response = requests.get(url, timeout=10)
        # Raise an error if the request was unsuccessful (e.g., 404, 500)
        response.raise_for_status()
        
        # Get the text content from the response
        doc_text = response.text

        # Return the text in a JSON format
        return jsonify({"code": doc_text})

    except requests.exceptions.RequestException as e:
        # Handle network errors or bad responses
        abort(500, description=f"Failed to fetch document. Error: {e}")

# This allows the app to be run directly for testing
if __name__ == '__main__':
    app.run(debug=True)