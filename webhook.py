# webhook/webhook.py - by:proxlu
from flask import Flask, request, jsonify

app = Flask(__name__)

# Variável para armazenar a última requisição POST
last_post_data = None

# Rota para receber requisições POST
@app.route('/webhook', methods=['POST'])
def handle_post():
    global last_post_data
    # Armazena o corpo da requisição POST
    last_post_data = request.get_json(force=True)  # Aceita JSON
    print('Nova requisição POST recebida:', last_post_data)
    return 'Requisição POST recebida com sucesso!', 200

# Rota para exibir a última requisição POST
@app.route('/webhook', methods=['GET'])
def handle_get():
    if last_post_data:
        # Retorna o último dado POST em formato JSON
        return jsonify(last_post_data), 200
    else:
        return 'Nenhum dado POST recebido ainda.', 404

# Inicia o servidor
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
