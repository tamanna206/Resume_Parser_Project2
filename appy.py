from flask import Flask, request, jsonify
import pdfplumber, spacy

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

@app.route("/parse_resume", methods=["POST"])
def parse_resume():
    file = request.files["resume"]
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return jsonify({"extracted": entities})

if __name__ == "__main__":
    app.run(debug=True)


