# app.py
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Carpeta donde se guardarán las imágenes
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Asegura que la carpeta 'uploads' exista
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Ruta para subir la imagen
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    image = request.files['image']

    if image.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if image:
        # Guardar la imagen en la carpeta 'uploads'
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))
        return jsonify({'message': 'Image uploaded successfully'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
