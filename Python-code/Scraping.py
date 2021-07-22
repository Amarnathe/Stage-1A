import requests
from bs4 import BeautifulSoup
import csv
import re
import time

# URLs
url_figaro = 'http://evene.lefigaro.fr/citations/theme/tous-les-themas.php'
url_dicocitation = 'https://www.dicocitations.com/dictionnaire-citations.php'

# Requests
html_fig = requests.get(url_figaro).text
html_dico = requests.get(url_dicocitation).text

# HTML
soupF = BeautifulSoup(html_fig, 'html.parser')
soupD = BeautifulSoup(html_dico, 'html.parser')

def Soup(url):
    html = requests.get(url).text
    #time.sleep(0.5)
    return BeautifulSoup(html, 'html.parser')


soupD = Soup(url_dicocitation)


### Creating CSV file ###

def to_csv(str, list1, list2, list3, list4, list5, list6):

    with open(str, 'w', newline='') as f:
        wr = csv.writer(f)
        wr.writerow(['Citations', 'Auteur', 'Source', 'Thèmes', "Nombre d'avis", "Notes"])

        for i in range(len(list1)):
            string = ""
            if len(list4[i]) > 1:
                for j in range(len(list4[i])):
                    if j == 0:
                        string = list4[i][j]
                    else:
                        string = string + ', ' + list4[i][j]
                wr.writerow([list1[i], list2[i], list3[i], string, list5[i], list6[i]])

            else:
                wr.writerow([list1[i], list2[i], list3[i], list4[i][0], list5[i], list6[i]])


###  Figaro  ###

soupF = Soup(url_figaro)

authors = []    # List of authors for each quote
citations = []  # List of quotes
links = []      # URL for another page of quotes
notes = []      # Note for each quote when there is a review
Nbavis = []     # Number of votes
source = []     # Source of each quote
themas = []     # List of themas
themes = []     # Theme for each quote


# Finding links and key words
div = soupF.find_all('div', class_='figsco__accordion figsco__accordion__on__tablet')[2]
A = div.find_all('a', href=True)                                                            # For getting URLs

for a in A:
    links.append(a.get('href'))                                                 # Gets URLs of different web pages
    themas.append(re.search(r"\b(\w+)$", a.get('href')).group().capitalize())   # Gets key words using Regex

# Collect data
k = 0

for u in links :
    soupF = Soup(u)
    next_page = 1

    while next_page == 1:

        # Lien de la page suivante
        Next = soupF.find(title="Aller à la page suivante")

        # Liste des citations Figaro
        cit = soupF.find_all(class_='figsco__quote__text')

        # Listes des Auteurs Figaro
        aut = soupF.find_all(class_="figsco__fake__col-9")

        # Extract the code of the review
        reviews = soupF.find_all('div', class_='figsco__review__note')

        # Number of quotes
        nb = len(aut)

        # for the number of quotes with a review
        nt = 0

        for i in range(nb):

            if (u == links[11]) & (i == 11):                      # for an empty section
                break

            name = aut[i].text.strip().replace("\r", "")          # strip() in order to remove '\n' in the string

            phrase = cit[i].text.strip().replace("\r", ". ")

            if citations.count(phrase) > 0:                       # When there is two same quotes
                themes[citations.index(phrase)].append(themas[k]) # Adding only the other theme
                continue

            else:
                themes.append([themas[k]])                  # Add the theme for the quote
                citations.append(phrase)                    # Add the quote

            if ('/' in name) :          # Structure of the string : "Author / Source Avis" or just "Author" or "Author / Avis"

                if len(name.split("/ ")) != 2:
                    authors.append(name.replace("/", ""))
                    source.append(None)
                    Nbavis.append(None)
                    notes.append(None)

                elif 'Vos avis' in name.split("/ ")[1]:
                    s = name.split("/ ")[1].replace(') :', "").split('            \n\nVos avis (')
                    authors.append(name.split("/ ")[0].replace("                    ", "").replace("De ", "").replace("\n", ""))
                    notes.append(str(reviews[nt]).count('_active'))
                    nt = nt + 1

                    if len(s) == 2:  # For the structure, we need 2 components
                        source.append(s[0].replace('            ', ""))
                        Nbavis.append(s[1])

                    else:
                        s = name.split("/ ")[1].replace(') :', "").split('\n                \nVos avis (')
                        source.append(s[0].replace('            ', ""))
                        Nbavis.append(s[1])

                else:
                    authors.append(name.split("/ ")[0].replace("                    ", "").replace("De ", "").replace("\n", ""))
                    source.append(name.split("/ ")[1])
                    Nbavis.append(None)
                    notes.append(None)

            else:
                source.append(None)
                ns = name.replace("                    ", "").replace("De ", "").replace("                  \n                ", "")

                if 'Vos avis' in ns:
                    n = ns.replace(') :', "").split('\nVos avis (')
                    notes.append(str(reviews[nt]).count('_active'))
                    nt = nt + 1

                    if len(n)<2:        # No author
                        authors.append('Anonyme')
                        Nbavis.append(n[0].replace('Vos avis (', ""))
                    else:
                        authors.append(n[0].replace("\n", "").replace("                 ", ""))
                        Nbavis.append(n[1])
                else:
                    if not('De' in name):
                        authors.append('Anonyme')

                    else:
                        authors.append(ns)
                    Nbavis.append(None)
                    notes.append(None)

        if Next != None:
            next_page = 1                   # len(Next)
            next_url = Next.get('href')     # gets the path to the next page
            soupF = Soup("http://evene.lefigaro.fr/" + next_url)

        else:
            next_page = 0                   # There is not another page

    k = k + 1

# print results
#print(citations)
#print(authors)
#print(source)
#print(themes)
#print(Nbavis)

# Check if all lists have the same shape
print(len(citations), len(authors), len(source), len(themes), len(Nbavis), len(notes))

# Creates the CSV file
to_csv("data.csv", citations, authors, source, themes, Nbavis, notes)


### DicoCitation ###
#    To Do      #
#####################