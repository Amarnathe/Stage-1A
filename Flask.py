from django.shortcuts import redirect
from flask import Flask, render_template, request, url_for
from flask_bootstrap5 import Bootstrap
import pandas as pd



data = pd.read_csv("/Users/amarnathe/Documents/Télécom/Stage/pythonProject/data.csv")


quotes = data["Citations"].tolist()
authors = data["Auteur"].tolist()
Source = data["Source"].tolist()
Theme = data["Thèmes"].tolist()
NbAvis = data["Nombre d'avis"].tolist()
Notes = data["Notes"].tolist()
N = len(quotes)
app = Flask(__name__)
Bootstrap(app)

@app.route("/")
@app.route("/home/")
def home():
    return render_template("home.html")

@app.route("/index/", methods=['GET', "POST"])
def index():
    word = request.form.get("keyword")
    author = request.form.get('author')
    theme = request.form.get('theme')
    Nmin = request.form.get('min')
    Nmax = request.form.get('max')
    quotes1 = []
    authors1 = []
    Source1 = []
    Theme1 = []
    NbAvis1 = []
    Notes1 = []

    if "Recherche" in request.form.values():
        for i in range(N):

            if word != '':
                if not(quotes[i] in quotes1) and ((str(word) in quotes[i]) or ((str(word) in str(quotes[i])) or (str(word) in str(authors[i])) or (str(word) in str(Source[i])) or (str(word) in str(Theme[i])))):
                    if author != '':
                        if author in str(authors[i]):
                            if theme != '' and theme in str(Theme[i]):
                                if not (quotes[i] in quotes1):
                                    quotes1.append(quotes[i])
                                    authors1.append(authors[i])
                                    Source1.append(Source[i])
                                    Theme1.append(Theme[i])
                                    NbAvis1.append(NbAvis[i])
                                    Notes1.append(Notes[i])
                    elif theme != '':
                        if theme in str(Theme[i]):
                            if not (quotes[i] in quotes1):
                                quotes1.append(quotes[i])
                                authors1.append(authors[i])
                                Source1.append(Source[i])
                                Theme1.append(Theme[i])
                                NbAvis1.append(NbAvis[i])
                                Notes1.append(Notes[i])
                    else:
                        if not (quotes[i] in quotes1):
                            quotes1.append(quotes[i])
                            authors1.append(authors[i])
                            Source1.append(Source[i])
                            Theme1.append(Theme[i])
                            NbAvis1.append(NbAvis[i])
                            Notes1.append(Notes[i])

            elif author != '' and author in str(authors[i]):
                if theme != '' and theme in str(Theme[i]):
                    if not (quotes[i] in quotes1):
                        quotes1.append(quotes[i])
                        authors1.append(authors[i])
                        Source1.append(Source[i])
                        Theme1.append(Theme[i])
                        NbAvis1.append(NbAvis[i])
                        Notes1.append(Notes[i])
            elif theme != '' and theme in str(Theme[i]):
                if not (quotes[i] in quotes1):
                    quotes1.append(quotes[i])
                    authors1.append(authors[i])
                    Source1.append(Source[i])
                    Theme1.append(Theme[i])
                    NbAvis1.append(NbAvis[i])
                    Notes1.append(Notes[i])

        if len(quotes1) == 0:
            return resultat(["Pas de résultat :("], ["Sorry"], ["nan"], ["/"], ["nan"], ["nan"])
        else:
            return resultat(quotes1, authors1, Source1, Theme1, NbAvis1, Notes1)
    else:
        return render_template("Index.html")


@app.route("/resultat/")
def resultat(quotes, authors, Source, Theme, NbAvis, Notes):
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
