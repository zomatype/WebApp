from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from app import db
from app.models import PDFFile

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  
db.init_app(app)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/api/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filename)

    pdf_file = PDFFile(filename=file.filename)
    db.session.add(pdf_file)
    db.session.commit()

    return jsonify({'message': 'File uploaded successfully'}), 200

@app.route('/api/files', methods=['GET'])
def get_files():
    files = PDFFile.query.all()
    file_list = [{'id': file.id, 'filename': file.filename} for file in files]
    return jsonify({'files': file_list}), 200

@app.route('/api/download/<filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
