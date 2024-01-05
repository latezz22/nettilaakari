from urllib import response
from flask import Flask, render_template, request, jsonify, make_response
from bot import luo_vastaus


app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

@app.post("/vastaa")
def vastaa():
    teksti = request.get_json()
    vastaus = luo_vastaus(teksti)

    return make_response(jsonify(vastaus))
    


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
    