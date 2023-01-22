from flask import Flask, request, Response

app = Flask(__name__)

num = {"numero": 0}

@app.route('/contador', methods=["GET"])
def conta():
    return num, 200

@app.route('/contador', methods=["POST"])
def operacao():
    global num
    num = request.json
    return num, 200

@app.route('/contador/incrementa', methods=["PUT"])
def incrementa():
    num["numero"] += 1
    return num, 202  

@app.route('/contador', methods=["DELETE"])
def deletar():
    num["numero"] = 0
    return num, 202  

if __name__ == "__main__":
    app.run(debug=True)