from flask import Flask, render_template, request, jsonify
import os
from ocr import ocrmodule
from ner import nermodule

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            text = ocrmodule(file_path)
            entities = nermodule(text)
            os.remove(file_path)
            return jsonify({'text': text, 'entities': entities})
        else:
            return jsonify({'error': 'No file provided'})

if __name__ == '__main__':
    app.run(debug=True)
