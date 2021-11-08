from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

def stemming(text):
    stem=[]
    ps = PorterStemmer()
    words = set(text.split())
    for w in words:
        print(w,":",ps.stem(w))
        stem.append(ps.stem(w))


#stemming("how running loving shiny")