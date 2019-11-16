from flask import Flask,render_template, url_for, flash, redirect, request, jsonify
from flask_socketio import SocketIO, emit, send


# Configuracion basica del servidor en Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = '9f3f918414c3b8f36c904aa6085d019c'
app.debug = True
app.host = '0.0.0.0'
socketio = SocketIO(app)


# Ruta por defecto en http://127.0.0.1:5000/
@app.route("/")
def hello():
   return render_template('bottles.html')

# SocketIO: aquí se manejan los mensajes entrantes
# y salientes del servidor, este es el socket que
# recibe las señales del archivo arduino.py
start = True

@socketio.on('proximity')
def handle_proximity(message):
   print('received message: ' + message)
   send(message, broadcast=True)


if __name__ == '__main__':
   socketio.run(app)
