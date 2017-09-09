from flask import Flask 
app = Flask(__name__)
@app.route("/") # Aqui es para poner la url que quiero, la lista de datos de temperatura
def hello():
	return "Hello World"


	#Una ruta por cada tabla de datos, una funcion para cada cosa
	#Los datos en json