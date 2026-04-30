from flask import Flask, request, render_template, jsonify
import os
import shutil

# Make sure to import from src.models.predict since the project uses this to classify
from src.models.predict import predict_multiple

app = Flask(__name__)
UPLOAD_DIR = "temp"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if 'files[]' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400
    
    files = request.files.getlist('files[]')
    if not files or files[0].filename == '':
        return jsonify({"error": "No selected file"}), 400

    file_paths = []
    for file in files:
        if file.filename:
            file_path = os.path.join(UPLOAD_DIR, file.filename)
            file.save(file_path)
            file_paths.append(file_path)
            
    try:
        # Calls the function from src.models.predict
        label, confidence = predict_multiple(file_paths)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({
        "prediction": label,
        "confidence": round(confidence * 100, 2),
        "num_files": len(file_paths)
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)
