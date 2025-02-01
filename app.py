from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("carregamento.html")

@app.route("/parabens")
def niver():
    return render_template("niver.html")

if __name__ == "__main__":
    app.run(debug=True)
#teste