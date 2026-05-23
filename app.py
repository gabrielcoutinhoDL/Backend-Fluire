from flask import Flask, jsonify, redirect, request
from flask_cors import CORS

#As rotas ficam aqui
#import route.tralala_routes import * 
#Fim das rotas

app = Flask(__name__)
CORS(app)


#Inicianlizando as rotas
#init_usuario_routes(app)
#Fim das rotas

if __name__ == 'main':
    app.run(debug=True)