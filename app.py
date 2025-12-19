from flask import Flask, jsonify, request

from helpers.cipher import generar_papa
from helpers.registro import registrar, verificar

app = Flask(__name__)

@app.route("/test", methods=["POST"])
# http://localhost:5000/test

def test_endpoint():
    
    uid = request.json.get("uid")

    sello = generar_papa(uid)
    registrar(sello)


    return jsonify({"sello": sello})


@app.route("/view", methods=["GET"])
# http://localhost:5000/view

def view_endpoint():

    sello = request.headers.get("X-MTS-SEAL")

    if not sello or not verificar(sello):
        return jsonify({"error": "no entramos we"}), 403

    return jsonify({"estado": "si entramos we"})


if __name__ == "__main__":
    app.run(debug=True)
    


