from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Intenta parsear el contenido como JSON
    try:
        data = request.get_json()
        print("Datos recibidos como JSON:")
        print(data)
    except:
        data = request.data
        print("Datos recibidos como texto plano o no JSON:")
        print(data)

    return "OK", 200

def procesar(data):
    # Aquí se procesa la información recibida
    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
