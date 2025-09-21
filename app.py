from flask import Flask, jsonify, abort
import requests

app = Flask(__name__)

DOCS = {
    "GP3": "your_google_doc_id_here"  # Replace this with your Doc ID
}

def fetch_doc_text(doc_id):
    url = f"https://docs.google.com/document/d/{doc_id1742fRLpPzyftgF5Cz9w0z3cXLRiH6JCY7ejXSoxzvlQ}/export?format=txt"
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    return r.text

@app.route("/get_code/<name>")
def get_code(name):
    doc_id = DOCS.get(name)
    if not doc_id:
        return abort(404, "name not found")
    try:
        text = fetch_doc_text(doc_id)
    except Exception as e:
        return abort(502, str(e))
    return jsonify({"code": text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
