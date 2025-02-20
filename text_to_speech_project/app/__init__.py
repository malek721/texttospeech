from flask import Flask
from app.routes import routes_bp
import os


def create_app():
    app = Flask(__name__, template_folder="../templates")

    # app.config['SECRET_KEY'] = 'your_secret_key'
    # Dosya yükleme klasörü (resimler)

    upload_folder = os.path.join(app.root_path, '..', 'static', 'uploads')
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
    app.config['UPLOAD_FOLDER'] = upload_folder

    # Plan kaydı
    app.register_blueprint(routes_bp)

    return app
