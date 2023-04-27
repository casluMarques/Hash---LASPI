from flask import Flask, request
import hashlib

app = Flask(__name__)

@app.route("/" , methods=['POST','GET'])
def form_laspi():
    if request.method == 'POST':
            arquivo = request.files["file"]
            ler_arquivo = arquivo.read()
            sha256hash = hashlib.sha256(ler_arquivo)
            sha256hashed = sha256hash.hexdigest()
            return '<h1> {} <h1> '.format(sha256hashed)
    return'''<h1> Deposite toda a documentação enviada: <h1> 
    <form method = 'POST' action = "" enctype = "multipart/form-data">
            <p><input type = "file" name = "file"><p>
            <p><input type = "submit"><p>
            </form> '''