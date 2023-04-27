from flask import Flask, request
import hashlib

def sha256sum(filename):
    h  = hashlib.sha256()
    b  = bytearray(128*1024)
    mv = memoryview(b)
    data = filename.read()
    h.update(data[:-1])
    return h.hexdigest()

app = Flask(__name__)

@app.route("/" , methods=['POST','GET'])
def form_laspi():
    if request.method == 'POST':
        result =[]
        arquivos = request.files["file"]
        print(arquivos)
        '''for arquivo in arquivos:
                result.append(sha256sum(arquivo))
        print(result)
        '''
        return '<h1> {} <h1> '.format(hash for hash in result)
    return'''<h1> Deposite toda a documentação enviada: <h1> 
    <form method = 'POST' action = "" enctype = "multipart/form-data">
            <p><input type = "file" name = "file" multiple ><p>
            <p><input type = "submit"><p>
            </form> '''