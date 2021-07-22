from flask import Flask, render_template, request
from flask_bootstrap5 import Bootstrap
import pandas as pd

data = pd.read_csv("/Users/amarnathe/Documents/Télécom/Stage/pythonProject/data.csv")


quotes = data["Citations"].tolist()
authors = data["Auteur"].tolist()
Source = data["Source"].tolist()
Theme = data["Thèmes"].tolist()
NbAvis = data["Nombre d'avis"].tolist()
Notes = data["Notes"].tolist()

app = Flask(__name__)
Bootstrap(app)
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/index/", methods=['GET', "POST"])
def index():
    word = request.form.get("keyword")
    author = request.form.get('author')
    theme = request.form.get('theme')
    Nmin = request.form.get('min')
    Nmax = request.form.get('max')
    if "Recherche" in request.form.values():
        return resultat()
    else:
        return render_template("index.html")
@app.route("/resultat/")
def resultat():
    return render_template("resultat.html", quotes = quotes, authors = authors, Source = Source, Theme = Theme, NbAvis=NbAvis, Notes=Notes)

@app.route("/page=2")
def page():
    return render_template("2.html")


@app.route("/search")
def search():
    return render_template("template.html")

if __name__ == "__main__":
    app.run(debug=True)

# framework
# react, angular
# send json au lieu de html
# citation :
# navigateur génère la page
