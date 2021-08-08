from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
import pandas as pd
import unicodedata
from sklearn.linear_model import LogisticRegression


# Vectorize the sentence
def vect(string, result):
    l = []
    for i in range(N):
        if result[i] in string.split():
            l.append(1)
        else:
            l.append(0)
    return l

# dimension of the vector
N = 4920

# Reading data
data = pd.read_csv("/Users/amarnathe/Documents/Télécom/Stage/pythonProject/data.csv")

# Extrating themes and authors
Themes = data["Thèmes"].tolist()
Authors = data["Auteur"].tolist()

port = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# Extrating quotes
d_list = data["Citations"].tolist()


# Removing accents
d_list = [''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')) for s in d_list]

# Removing special characters and Stemming
d_list = [" ".join([port.stem(word.replace(".", "").replace('“', "").replace("”", "").replace('+', "").replace(']', "").replace("[", "").replace(";", "").replace(':', "").replace('%', "").replace('"', "").replace(')', "").replace('(', "").replace("!", "").replace("?", "").replace("'", " ").replace("’", " ").replace("-", " ").replace(",", "")) for word in doc.split()]) for doc in d_list]

# list of stop words
stop_words = set(stopwords.words('french'))

# Removing stop words
result = []
for data in d_list:
    words = data.split()
    for r in words:
        if not r.lower() in stop_words:
            r = lemmatizer.lemmatize(r)
            result.append(r)


result = sorted(list(set(result)))


# Vectorizing each quote
pipe = Pipeline([('count', CountVectorizer(vocabulary=result)), ('tfid', TfidfTransformer())]).fit(d_list)

# TF-IDF array
TF_IDF = pipe['count'].transform(d_list).toarray()/pipe['tfid'].idf_


# Adding the column target : Themes
#TF_IDF = np.hstack((TF_IDF, np.atleast_2d(np.array(Themes)).T))

# Training and testing data
x_train = TF_IDF[0:3077, :N]
x_test = TF_IDF[3078:3846, :N]
y_train = Themes[0:3077]    #TF_IDF[0:3077, 6315:6316]
y_test = Themes[3078:3846]  #TF_IDF[3078:3846, 6315:6316]

y1_train = Authors[0:3077]
y1_test = Authors[3078:3846]

# Logistic Regression models
LRT = LogisticRegression(random_state=0, solver='liblinear', multi_class='auto')
LRA = LogisticRegression(random_state=0, solver='liblinear', multi_class='auto')

model_T = LRT.fit(x_train, y_train)
model_A = LRA.fit(x_train, y1_train)

precision_T = LRT.score(x_test, y_test)
precision_A = LRA.score(x_test, y1_test)

#print("précision A", precision_A*100)
#print("précision_T", precision_T*100)

### Input String ###
# Predict the theme of this sting value
string = d_list[0]
string_Vec = vect(string.replace(".", "").replace('“', "").replace("”", "").replace('+', "").replace(']', "").replace("[", "").replace(";", "").replace(':', "").replace('%', "").replace('"', "").replace(')', "").replace('(', "").replace("!", "").replace("?", "").replace("'", " ").replace("’", " ").replace("-", " ").replace(",", ""), result)

#prediction
prediction_T = model_T.predict([string_Vec])
prediction_A = model_A.predict([string_Vec])

print("prédiction T: ", prediction_T)
#print("prédiction A: ", prediction_A)

#print(d_list[0], "\n", Themes[0], "\n", Authors[0])


#prédiction
#prediction = model.predict([[20,4.3,5.5]])
#nom_fruit_cible[prediction[0]]
