from flask import Flask, jsonify
import random
from bd import Conselhos
import json

app = Flask(__name__)

# Rota para retornar os dados de forma aleatória
@app.route('/api/conselhos', methods=['GET'])
def get_conselhos_aleatorios():
    conselhos_aleatorios = random.sample(Conselhos, 1)  # Retorna 1 conselho aleatório
    json_data = json.dumps(conselhos_aleatorios, ensure_ascii=False)
    return json_data

if __name__ == '__main__':
    app.run(debug=True)
