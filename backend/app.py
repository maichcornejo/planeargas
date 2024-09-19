from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "¡Bienvenidos al backend de Planear Gas!"

if __name__ == '__main__':
<<<<<<< HEAD
    app.run(host='0.0.0.0', port=8080)
=======
    app.run(host='0.0.0.0', port=8080)
>>>>>>> 366618d8 (primer actualizacion melli)
