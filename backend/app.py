from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "¡Bienvenidos al backend de Planear Gas!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
