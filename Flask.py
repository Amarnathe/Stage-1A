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

        if word!='' and author !='' and theme !='':
            wordUp = word[0].capitalize() + word[1:]    # To consider the first capital letter
            if Nmin != "" and Nmax != "" and Nmin <= Nmax:
                for i in range(N):
                    if not(quotes[i] in quotes1) and (((str(word) in quotes[i]) or ((str(word) in str(quotes[i])) or (str(word) in str(authors[i])) or (str(word) in str(Source[i])) or (str(word) in str(Theme[i])))) or ((str(wordUp) in quotes[i]) or ((str(wordUp) in str(quotes[i])) or (str(wordUp) in str(authors[i])) or (str(wordUp) in str(Source[i])) or (str(wordUp) in str(Theme[i]))))):
                        if author in str(authors[i]):
                            if theme in str(Theme[i]):
                                if str(Notes[i]) != "nan":
                                    if not (quotes[i] in quotes1) and Nmin<=str(int(Notes[i])) and Nmax>=str(int(Notes[i])):
                                        quotes1.append(quotes[i])
                                        authors1.append(authors[i])
                                        Source1.append(Source[i])
                                        Theme1.append(Theme[i])
                                        NbAvis1.append(NbAvis[i])
                                        Notes1.append(Notes[i])
            else: #or "else"
                for i in range(N):
                    if not(quotes[i] in quotes1) and (((str(word) in quotes[i]) or ((str(word) in str(quotes[i])) or (str(word) in str(authors[i])) or (str(word) in str(Source[i])) or (str(word) in str(Theme[i])))) or ((str(wordUp) in quotes[i]) or ((str(wordUp) in str(quotes[i])) or (str(wordUp) in str(authors[i])) or (str(wordUp) in str(Source[i])) or (str(wordUp) in str(Theme[i]))))):
                        if author in str(authors[i]):
                            if theme in str(Theme[i]):
                                quotes1.append(quotes[i])
                                authors1.append(authors[i])
                                Source1.append(Source[i])
                                Theme1.append(Theme[i])
                                NbAvis1.append(NbAvis[i])
                                Notes1.append(Notes[i])
                        
        elif word!='' and author !='' and theme =='':
            wordUp = word[0].capitalize() + word[1:]    # To consider the first capital letter
            if Nmin != "" and Nmax != "" and Nmin <= Nmax:
                for i in range(N):
                    if not(quotes[i] in quotes1) and (((str(word) in quotes[i]) or ((str(word) in str(quotes[i])) or (str(word) in str(authors[i])) or (str(word) in str(Source[i])) or (str(word) in str(Theme[i])))) or ((str(wordUp) in quotes[i]) or ((str(wordUp) in str(quotes[i])) or (str(wordUp) in str(authors[i])) or (str(wordUp) in str(Source[i])) or (str(wordUp) in str(Theme[i]))))):
                        if author in str(authors[i]):
                            if str(Notes[i])!="nan":
                                if not (quotes[i] in quotes1) and Nmin<=str(int(Notes[i])) and Nmax>=str(int(Notes[i])): 
                                    quotes1.append(quotes[i])
                                    authors1.append(authors[i])
                                    Source1.append(Source[i])
                                    Theme1.append(Theme[i])
                                    NbAvis1.append(NbAvis[i])
                                    Notes1.append(Notes[i])
            elif Nmin == "" and Nmax == "" :
                for i in range(N):
                    if not(quotes[i] in quotes1) and (((str(word) in quotes[i]) or ((str(word) in str(quotes[i])) or (str(word) in str(authors[i])) or (str(word) in str(Source[i])) or (str(word) in str(Theme[i])))) or ((str(wordUp) in quotes[i]) or ((str(wordUp) in str(quotes[i])) or (str(wordUp) in str(authors[i])) or (str(wordUp) in str(Source[i])) or (str(wordUp) in str(Theme[i]))))):
                        if author in str(authors[i]):
                            quotes1.append(quotes[i])
                            authors1.append(authors[i])
                            Source1.append(Source[i])
                            Theme1.append(Theme[i])
                            NbAvis1.append(NbAvis[i])
                            Notes1.append(Notes[i])
        elif word!='' and author =='' and theme !='':
            wordUp = word[0].capitalize() + word[1:]    #To consider the first capital letter
            if Nmin != "" and Nmax != "" and Nmin <= Nmax:
                for i in range(N):
                    if not(quotes[i] in quotes1) and (((str(word) in quotes[i]) or ((str(word) in str(quotes[i])) or (str(word) in str(authors[i])) or (str(word) in str(Source[i])) or (str(word) in str(Theme[i])))) or ((str(wordUp) in quotes[i]) or ((str(wordUp) in str(quotes[i])) or (str(wordUp) in str(authors[i])) or (str(wordUp) in str(Source[i])) or (str(wordUp) in str(Theme[i]))))):
                        if theme in str(Theme[i]):
                            if str(Notes[i])!="nan":
                                if not (quotes[i] in quotes1) and Nmin<=str(int(Notes[i])) and Nmax>=str(int(Notes[i])): 
                                    quotes1.append(quotes[i])
                                    authors1.append(authors[i])
                                    Source1.append(Source[i])
                                    Theme1.append(Theme[i])
                                    NbAvis1.append(NbAvis[i])
                                    Notes1.append(Notes[i])
            elif Nmin == "" and Nmax == "" :
                for i in range(N):
                    if not(quotes[i] in quotes1) and (((str(word) in quotes[i]) or ((str(word) in str(quotes[i])) or (str(word) in str(authors[i])) or (str(word) in str(Source[i])) or (str(word) in str(Theme[i])))) or ((str(wordUp) in quotes[i]) or ((str(wordUp) in str(quotes[i])) or (str(wordUp) in str(authors[i])) or (str(wordUp) in str(Source[i])) or (str(wordUp) in str(Theme[i]))))):
                        if theme in str(Theme[i]):
                            quotes1.append(quotes[i])
                            authors1.append(authors[i])
                            Source1.append(Source[i])
                            Theme1.append(Theme[i])
                            NbAvis1.append(NbAvis[i])
                            Notes1.append(Notes[i])
        elif word!='' and author =='' and theme =='':
            wordUp = word[0].capitalize() + word[1:]    # To consider the first capital letter
            if Nmin != "" and Nmax != "" and Nmin <= Nmax:
                for i in range(N):
                    if not(quotes[i] in quotes1) and (((str(word) in quotes[i]) or ((str(word) in str(quotes[i])) or (str(word) in str(authors[i])) or (str(word) in str(Source[i])) or (str(word) in str(Theme[i])))) or ((str(wordUp) in quotes[i]) or ((str(wordUp) in str(quotes[i])) or (str(wordUp) in str(authors[i])) or (str(wordUp) in str(Source[i])) or (str(wordUp) in str(Theme[i]))))):
                        if str(Notes[i])!="nan":
                            if not (quotes[i] in quotes1) and Nmin<=str(int(Notes[i])) and Nmax>=str(int(Notes[i])): 
                                quotes1.append(quotes[i])
                                authors1.append(authors[i])
                                Source1.append(Source[i])
                                Theme1.append(Theme[i])
                                NbAvis1.append(NbAvis[i])
                                Notes1.append(Notes[i])
            elif Nmin == "" and Nmax == "" :
                for i in range(N):
                    if not(quotes[i] in quotes1) and (((str(word) in quotes[i]) or ((str(word) in str(quotes[i])) or (str(word) in str(authors[i])) or (str(word) in str(Source[i])) or (str(word) in str(Theme[i])))) or ((str(wordUp) in quotes[i]) or ((str(wordUp) in str(quotes[i])) or (str(wordUp) in str(authors[i])) or (str(wordUp) in str(Source[i])) or (str(wordUp) in str(Theme[i]))))):
                        quotes1.append(quotes[i])
                        authors1.append(authors[i])
                        Source1.append(Source[i])
                        Theme1.append(Theme[i])
                        NbAvis1.append(NbAvis[i])
                        Notes1.append(Notes[i])
                                
        elif word=='' and author !='' and theme !='':
            print("1........")
            if Nmin != "" and Nmax != "" and Nmin <= Nmax:
                for i in range(N):
                    if not(quotes[i] in quotes1) :
                        if author in str(authors[i]):
                            if theme in str(Theme[i]):
                                if str(Notes[i])!="nan":
                                    if not (quotes[i] in quotes1) and Nmin<=str(int(Notes[i])) and Nmax>=str(int(Notes[i])): 
                                        quotes1.append(quotes[i])
                                        authors1.append(authors[i])
                                        Source1.append(Source[i])
                                        Theme1.append(Theme[i])
                                        NbAvis1.append(NbAvis[i])
                                        Notes1.append(Notes[i])
            elif Nmin == "" and Nmax == "":
                for i in range(N):
                    if not(quotes[i] in quotes1):
                        if author in str(authors[i]):
                            if theme in str(Theme[i]):
                                quotes1.append(quotes[i])
                                authors1.append(authors[i])
                                Source1.append(Source[i])
                                Theme1.append(Theme[i])
                                NbAvis1.append(NbAvis[i])
                                Notes1.append(Notes[i])
        elif word=='' and author =='' and theme !='':
            if Nmin != "" and Nmax != "" and Nmin <= Nmax:
                for i in range(N):
                    if not(quotes[i] in quotes1) :
                        if theme in str(Theme[i]):
                            if str(Notes[i])!="nan":
                                if not (quotes[i] in quotes1) and Nmin<=str(int(Notes[i])) and Nmax>=str(int(Notes[i])): 
                                    quotes1.append(quotes[i])
                                    authors1.append(authors[i])
                                    Source1.append(Source[i])
                                    Theme1.append(Theme[i])
                                    NbAvis1.append(NbAvis[i])
                                    Notes1.append(Notes[i])
            elif Nmin == "" and Nmax == "" :
                for i in range(N):
                    if not(quotes[i] in quotes1) and (((str(word) in quotes[i]) or ((str(word) in str(quotes[i])) or (str(word) in str(authors[i])) or (str(word) in str(Source[i])) or (str(word) in str(Theme[i])))) or ((str(wordUp) in quotes[i]) or ((str(wordUp) in str(quotes[i])) or (str(wordUp) in str(authors[i])) or (str(wordUp) in str(Source[i])) or (str(wordUp) in str(Theme[i]))))):
                        if theme in str(Theme[i]):
                            quotes1.append(quotes[i])
                            authors1.append(authors[i])
                            Source1.append(Source[i])
                            Theme1.append(Theme[i])
                            NbAvis1.append(NbAvis[i])
                            Notes1.append(Notes[i])
        elif word=='' and author !='' and theme =='':
            if Nmin != "" and Nmax != "" and Nmin <= Nmax:
                for i in range(N):
                    if not(quotes[i] in quotes1) :
                        if author in str(authors[i]):
                            if str(Notes[i])!="nan":
                                if not (quotes[i] in quotes1) and Nmin<=str(int(Notes[i])) and Nmax>=str(int(Notes[i])): 
                                    quotes1.append(quotes[i])
                                    authors1.append(authors[i])
                                    Source1.append(Source[i])
                                    Theme1.append(Theme[i])
                                    NbAvis1.append(NbAvis[i])
                                    Notes1.append(Notes[i])
            elif Nmin == "" and Nmax == "":
                for i in range(N):
                    if not(quotes[i] in quotes1) and (((str(word) in quotes[i]) or ((str(word) in str(quotes[i])) or (str(word) in str(authors[i])) or (str(word) in str(Source[i])) or (str(word) in str(Theme[i])))) or ((str(wordUp) in quotes[i]) or ((str(wordUp) in str(quotes[i])) or (str(wordUp) in str(authors[i])) or (str(wordUp) in str(Source[i])) or (str(wordUp) in str(Theme[i]))))):
                        if author in str(authors[i]):
                            if str(Notes[i])!="nan":
                                quotes1.append(quotes[i])
                                authors1.append(authors[i])
                                Source1.append(Source[i])
                                Theme1.append(Theme[i])
                                NbAvis1.append(NbAvis[i])
                                Notes1.append(Notes[i])

        elif word=='' and author =='' and theme =='':
            if Nmin != "" and Nmax != "" and Nmin <= Nmax:
                for i in range(N):
                    if str(Notes[i]) != "nan":
                        if not (quotes[i] in quotes1) and Nmin <= str(int(Notes[i])) and Nmax >= str(int(Notes[i])):

                            quotes1.append(quotes[i])
                            authors1.append(authors[i])
                            Source1.append(Source[i])
                            Theme1.append(Theme[i])
                            NbAvis1.append(NbAvis[i])
                            Notes1.append(Notes[i])


        if len(quotes1) == 0 or (Nmin != "" and Nmax != "" and Nmin > Nmax):
            return resultat(["Pas de résultat :("], ["Sorry"], ["nan"], ["/"], ["nan"], ["nan"])

        else:
            return resultat(quotes1, authors1, Source1, Theme1, NbAvis1, Notes1)
    else:
        return render_template("Index.html")

@app.route("/resultat/")
def resultat(quotes, authors, Source, Theme, NbAvis, Notes):
    return render_template("resultat.html", quotes=quotes, authors=authors, Source=Source, Theme=Theme, NbAvis=NbAvis, Notes=Notes)

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
