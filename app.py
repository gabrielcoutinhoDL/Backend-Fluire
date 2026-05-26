from flask import Flask
from flask_cors import CORS
from routes.alunos_routes import *
from routes.painel_routes import painel_bp


app = Flask(__name__)
CORS(app)
app.register_blueprint(alunos_bp)
app.register_blueprint(painel_bp)

if __name__ == '__main__':
    app.run(debug=True, 
            host='0.0.0.0', 
            port=5000)