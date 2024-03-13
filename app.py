from flask import Flask, jsonify
import random
from bd import Conselhos
app = Flask(__name__)

# Rota para retornar os dados de forma aleatória
@app.route('/api/conselhos', methods=['GET'])
def get_Conselhos_aleatorios():
    Conselhos_aleatorios = random.sample(Conselhos, 1)  # Retorna 1 conselho aleatório
    
    return jsonify(Conselhos_aleatorios)

if __name__ == '_main_':
    app.run(debug=True)