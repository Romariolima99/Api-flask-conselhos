from flask import Flask, jsonify
import random

app = Flask(__name__)

# Dados de exemplo
objetos = [
    {"id": 1, "nome": "Objeto 1", "descricao": "Descrição do objeto 1"},
    {"id": 2, "nome": "Objeto 2", "descricao": "Descrição do objeto 2"},
    # Adicione mais objetos aqui...
    {"id": 20, "nome": "Objeto 20", "descricao": "Descrição do objeto 20"}
]

# Rota para retornar os dados de forma aleatória
@app.route('/api/objetos', methods=['GET'])
def get_objetos_aleatorios():
    objetos_aleatorios = random.sample(objetos, 1)  # Retorna 5 objetos aleatórios
    
    return jsonify(objetos_aleatorios)

if __name__ == '_main_':
    app.run(debug=True)