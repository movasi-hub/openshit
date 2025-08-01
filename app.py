from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "¡Hola desde OpenShift Developer Sandbox!"

@app.route('/multiplicar', methods=['GET'])
def multiplicar():
    try:
        # Obtener los parámetros de la URL
        a = int(request.args.get('a'))
        b = int(request.args.get('b'))
        resultado = a * b
        return jsonify({
            'a': a,
            'b': b,
            'resultado': resultado
        }), 200
    except (TypeError, ValueError):
        return jsonify({'error': 'Parámetros inválidos. Se esperaban dos enteros.'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
