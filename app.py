from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Busca automáticamente en la carpeta 'templates'
    return render_template('index.html')

if __name__ == '__main__':
    # host='0.0.0.0' permite acceso desde otros dispositivos en la red local
    app.run(debug=True, port=5000)
