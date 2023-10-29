from  flask import Flask, render_template

app = Flask(__name__)

app.secret_key = "Utec"

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/")   
def clienteTabla():
    return render_template("Usuarios.html")


@app.route("/Sensores")   
def vendedorGrafico():
    return render_template("Sensores.html")

@app.route("/password.html")
def password():
    return render_template("password.html")

@app.route("/register.html")
def register():
    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True, port=3000)
