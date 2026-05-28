from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from flask_mail import Mail


from routes.usuarios_routes import usuarios_bp
from routes.aulas_routes import *
from routes.alunos_routes import *
from routes.frequencias_routes import frequencia_bp

load_dotenv()

app = Flask(__name__)

CORS(app)

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