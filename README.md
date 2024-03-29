# API de Conselhos Aleatórios

- Bem-vindo à API de Conselhos Aleatórios! Esta API foi desenvolvida utilizando Flask e retorna objetos contendo conselhos de forma aleatória.

- Endpoints
- localhost/api/conselhos
- Este endpoint retorna um objeto JSON contendo um conselho aleatório.

- methods=['GET']
- GET /api/conselhos

# Exemplo de resposta:

<img src="https://i.imgur.com/NBoTDIx.png" alt="GIF" data-canonical-src="https://i.imgur.com/NBoTDIx.png" style="max-width: 50%;">

`[{"slip": {"id": 13, "conselho": "Pratique a empatia, coloque-se no lugar dos outros."}}]`

# Como Usar
- Faça uma requisição GET para o endpoint localhost/api/conselhos
- Receba um conselho aleatório no formato JSON como resposta.

# Executando Localmente
- Certifique-se de ter o Python instalado em seu sistema. Você pode baixá-lo em python.org.

- Clone este repositório:

```js
    git clone https://github.com/Romariolima99/Api-flask-conselhos
 ```

 - Execute a aplicação:

 ```js
     flask run
 ```

<img src="https://i.imgur.com/j79b1Jm.png" alt="GIF" data-canonical-src="https://i.imgur.com/j79b1Jm.png" style="max-width: 50%;">