from flask import Flask, render_template #importamos flask desde el fremwork Flalsk

app = Flask(__name__) #inicializamos flask

#importacion y uso de escape para parametros para evitar injecciones de sql
from markupsafe import escape
#@app.route('/escape/<path:variable>')
#def escape(variable):
#    return f"<h1>{escape(variable)}</h1>"

@app.route('/') #creamos la ruta raiz 
def home():
    return render_template('index.html')

@app.route('/tutoriales') #creamos la ruta raiz 
def tuto():
    return render_template('tutoriales.html')

@app.route('/contacto') #creamos la ruta raiz 
def contact(): #podemos gregar variables de trabajo
    lista = ["uno", "dos", "tres", "cuatro"]
    return render_template('contacto.html', lista = lista)