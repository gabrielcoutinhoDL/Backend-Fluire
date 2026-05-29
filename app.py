from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from flask_mail import Mail
from extensions.jwt_config import init_jwt
from config.settings import Config
from routes.aulas_routes import *
from routes.alunos_routes import *
from routes.frequencias_routes import frequencia_bp
from routes.usuarios_routes import usuarios_bp
import os


load_dotenv()
app = Flask(__name__)

CORS(app)

# configurações do JWT
app.config.from_object(Config)

# inicializa JWT
init_jwt(app)

# flask-mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USENAME'] = os.getenv('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.getenv('EMAIL_PASSWORD')


app.register_blueprint(alunos_bp)
app.register_blueprint(aulas_bp)
app.register_blueprint(usuarios_bp)
app.register_blueprint(frequencia_bp)


if __name__ == '__main__':
    app.run(debug=True, 
        host='0.0.0.0', 
        port=5000,
        threaded=True
    )