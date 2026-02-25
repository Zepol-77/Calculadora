from flask import Flask, jsonify
from flask_cors import CORS
import math as mt
from flask import jsonify
app=Flask(__name__)
CORS(app)

## suma
@app.route("/")
@app.route("/<float:numero1>/<float:numero2>")
@app.route("/<int:numero1>/<int:numero2>")
@app.route("/<int:numero1>/<float:numero2>")
@app.route("/<float:numero1>/<int:numero2>")
def suma(numero1=0,numero2=0):
    resultado=numero1+numero2
    ##return f"<h1>el resultado es: {resultado}</h1> <hr>"
    data={
        "resultado":resultado,
        "operacion":"suma",
    }
    return jsonify(data)

## resta 
@app.route("/resta/<float:numero1>/<float:numero2>")
@app.route("/resta/<int:numero1>/<int:numero2>")
@app.route("/resta/<int:numero1>/<float:numero2>")
@app.route("/resta/<float:numero1>/<int:numero2>")
def resta(numero1=0,numero2=0):
    resultado=numero1-numero2
    ##return f"<h1>El resultado es: {Resultado}</h1> <hr>"
    resultado=numero1-numero2
    data={
        "Resultado": resultado,
        "Operacion": "Resta",
     }
    return jsonify(data)

##Multiplicacion
@app.route("/multiplicacion/<float:numero1>/<float:numero2>")
@app.route("/multiplicacion/<int:numero1>/<int:numero2>")
@app.route("/multiplicacion/<int:numero1>/<float:numero2>")
@app.route("/multiplicacion/<float:numero1>/<float:numero2>")
def multiplicacion(numero1=0,numero2=0):
    ##return f"<h1>El resultado es: {Resultado}</h1> <hr>"
    resultado=numero1*numero2
    data={
        "Resultado": resultado,
        "Operacion": "Multiplicacion",
     }
    return jsonify(data)

##Division
@app.route("/division/<float:numero1>/<float:numero2>")
@app.route("/division/<int:numero1>/<int:numero2>")
@app.route("/division/<int:numero1>/<float:numero2>")
@app.route("/division/<float:numero1>/<float:numero2>")
def division(numero1=0,numero2=0):
    ##return f"<h1>El resultado es: {Resultado}</h1> <hr>"
    resultado=numero1/numero2
    data={
        "Resultado": resultado,
        "Operacion": "Division",
     }
    return jsonify(data)
##Potenciacion
@app.route("/potenciacion/<float:numero1>/<float:numero2>")
@app.route("/potenciacion/<int:numero1>/<int:numero2>")
@app.route("/potenciacion/<int:numero1>/<float:numero2>")
@app.route("/potenciacion/<float:numero1>/<float:numero2>")
def potenciacion(numero1=0,numero2=0):
    ##return f"<h1>El resultado es: {Resultado}</h1> <hr>"
    resultado=numero1**numero2
    data={
        "Resultado": resultado,
        "Operacion": "Potenciacion",
     }
    return jsonify(data)
##Seno
@app.route("/seno/<float:numero1>")
@app.route("/seno/<int:numero1>")
def seno(numero1=0):
    ##return f"<h1>El resultado es: {Resultado}</h1> <hr>"
    resultado=mt.sin(numero1)
    data={
        "Resultado": resultado,
        "Operacion": "Seno",
     }
    return jsonify(data)
##Coseno
@app.route("/coseno/<float:numero1>")
@app.route("/coseno/<int:numero1>")
def coseno(numero1=0):
    ##return f"<h1>El resultado es: {Resultado}</h1> <hr>"
    resultado=mt.cos(numero1)
    data={
        "Resultado": resultado,
        "Operacion": "Coseno",
     }
    return jsonify(data)
if __name__=="__main__":
    ##El valor True indica que la app se dejara en modo debug
    app.run(debug=True)





