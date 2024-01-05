#Tuodaan oleelliset kirjastot

from urllib import response
from flask import Flask, render_template, request, jsonify, make_response
from bot import luo_vastaus


app = Flask(__name__) 

#Tuodaan Flaskille tietoon html tiedosto

@app.get("/")
def index():
    return render_template("index.html")

#Alustetaan funktio tiedon välitykseen

@app.post("/vastaa")
def vastaa():

    teksti = request.get_json()
    #Käytetään vastaus toisen python tiedoston kautta
    vastaus = luo_vastaus(teksti)

    #Palautetaan selaimelle
    return make_response(jsonify(vastaus))
    


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
    
