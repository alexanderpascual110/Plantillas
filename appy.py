from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    alumnos = ["Jan Perez", "Roberto Linares", "Sandra Cuevas"]
    return render_template("index.html",creador="Alexander Pascual Chapol",nombres = alumnos)

@app.route("/crearcuenta")
def crear_cuenta():
    return render_template("crearcuenta.html")

if __name__=="__main__":
    app.run(debug=True)
