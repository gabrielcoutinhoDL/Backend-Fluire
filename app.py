from flask import Flask
from flask_cors import CORS
from routes.alunos_routes import *
from routes.aulas_routes import *

#As rotas ficam aqui
#import route.tralala_routes import *
#Fim das rotas

app = Flask(__name__)
CORS(app)
app.register_blueprint(alunos_bp)
app.register_blueprint(aulas_bp)

#Inicianlizando as rotas
#init_usuario_routes(app)
#Fim da inicialização das rotas

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)