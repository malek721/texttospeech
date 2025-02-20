import os
from flask import Blueprint, request, render_template, current_app
from app.ocr import extract_text_from_image

routes_bp = Blueprint('routes_bp', __name__)

@routes_bp.route('/', methods=['GET', 'POST'])
def index():
    extracted_text = None
    if request.method == 'POST':
        image_file = request.files.get('image_file')

        # Dosyanın var olduğunu ve doğru olduğunu doğrulayın
        if not image_file or image_file.filename == '':
            return "Hiçbir dosya yüklenmedi", 400

        # Resmi kaydedin ve metni çıkarın
        img_path = os.path.join(current_app.config['UPLOAD_FOLDER'], image_file.filename)
        image_file.save(img_path)
        extracted_text = extract_text_from_image(img_path, lang='tur+eng')

    return render_template('index.html', extracted_text=extracted_text)