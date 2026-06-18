# API REST de carros - disponibiliza recursos via endpoints HTTP (CRUD completo)

from flask import Flask, jsonify, make_response, request
from bd import Carros

app = Flask('carros')


# GET - lista todos os carros
@app.route('/carros', methods=['GET'])
def get_carros():
    return jsonify(Carros)


# GET por ID - retorna um carro especifico
@app.route('/carros/<int:id>', methods=['GET'])
def get_carro_id(id):
    for carro in Carros:
        if carro.get('id') == id:
            return jsonify(carro)
    return make_response(jsonify(mensagem='Carro nao encontrado'), 404)


# POST - cria um novo carro
@app.route('/carros', methods=['POST'])
def criar_carro():
    carro = request.get_json()
    Carros.append(carro)
    return make_response(
        jsonify(mensagem='Carro cadastrado com sucesso!', carro=carro),
        201
    )


# PUT - edita um carro existente pelo ID
@app.route('/carros/<int:id>', methods=['PUT'])
def editar_carro_id(id):
    carro_alterado = request.get_json()
    for indice, carro in enumerate(Carros):
        if carro.get('id') == id:
            Carros[indice].update(carro_alterado)
            return jsonify(Carros[indice])
    return make_response(jsonify(mensagem='Carro nao encontrado'), 404)


# DELETE - remove um carro pelo ID
@app.route('/carros/<int:id>', methods=['DELETE'])
def excluir_carro(id):
    for indice, carro in enumerate(Carros):
        if carro.get('id') == id:
            del Carros[indice]
            return jsonify(mensagem='Carro excluido com sucesso!')
    return make_response(jsonify(mensagem='Carro nao encontrado'), 404)


if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)
