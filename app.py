from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sumar', methods=['GET'])
def sumar():
    try:
        a = int(request.args.get('a'))
        b = int(request.args.get('b'))
        return jsonify({'operacion': 'suma', 'a': a, 'b': b, 'resultado': a + b})
    except (TypeError, ValueError):
        return jsonify({'error': 'Parámetros inválidos'}), 400

@app.route('/restar', methods=['GET'])
def restar():
    try:
        a = int(request.args.get('a'))
        b = int(request.args.get('b'))
        return jsonify({'operacion': 'resta', 'a': a, 'b': b, 'resultado': a - b})
    except (TypeError, ValueError):
        return jsonify({'error': 'Parámetros inválidos'}), 400

@app.route('/multiplicar', methods=['GET'])
def multiplicar():
    try:
        a = int(request.args.get('a'))
        b = int(request.args.get('b'))
        return jsonify({'operacion': 'multiplicación', 'a': a, 'b': b, 'resultado': a * b})
    except (TypeError, ValueError):
        return jsonify({'error': 'Parámetros inválidos'}), 400

@app.route('/dividir', methods=['GET'])
def dividir():
    try:
        a = int(request.args.get('a'))
        b = int(request.args.get('b'))
        if b == 0:
            return jsonify({'error': 'División entre cero no permitida'}), 400
        return jsonify({'operacion': 'división', 'a': a, 'b': b, 'resultado': a / b})
    except (TypeError, ValueError):
        return jsonify({'error': 'Parámetros inválidos'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
