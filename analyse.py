from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem.snowball import FrenchStemmer
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline

stemmer = SnowballStemmer(language='french')

lemmatizer = WordNetLemmatizer()

test1 = """Je mange des pommes.""".replace(".", "").replace("'", " ")
test2 = """Tu manges des poires.""".replace(".", "").replace("'", " ")
test3 = """J'achète une pomme.""".replace(".", "").replace("'", " ")
d_list = [test1, test2, test3]

# word_tokenize accepts
# a string as an input, not a file.
stop_words = set(stopwords.words('french'))

result = []
for data in d_list:
    words = data.split()
    for r in words:
        if not r.lower() in stop_words:
            #r = lemmatizer.lemmatize(r)
            result.append(r)

result = sorted(list(set(result)))
print(result)

pipe = Pipeline([('count', CountVectorizer(vocabulary=result)), ('tfid', TfidfTransformer())]).fit(d_list)
print(pipe['count'].transform(d_list).toarray())
print(pipe['tfid'].idf_)
