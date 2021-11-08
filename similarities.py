import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import euclidean_distances


def cosine_sim(text1,text2,mode):
    document=[text1,text2]
    if mode=='B':
        cv=CountVectorizer()
        cv.fit(document)
        print("\nVocabulary: ", cv.vocabulary_)
        count_matrix = cv.transform(document)
        print("\nEncoded Document is:")
        print(count_matrix.toarray())
    else:
        vectorizer=TfidfVectorizer()
        count_matrix = vectorizer.fit_transform(document)
        print("\nVocabulary: ",vectorizer.get_feature_names())
        print("\nEncoded Document is:")
        print(count_matrix.toarray())

    cos_sim=cosine_similarity(count_matrix)
    return cos_sim[0][1]
    

def euclidean_sim(text1,text2):
    document=[text1,text2]
    vectorizer=TfidfVectorizer()
    count_matrix=vectorizer.fit_transform(document)
    print("tf-idf matrix is: ")
    print(count_matrix[0].toarray(),"\n",count_matrix[1].toarray())
    return euclidean_distances(count_matrix)[0][1]

def jaccard_sim(text1,text2):
    a = set(text1.split()) 
    b = set(text2.split())
    c = a.intersection(b)
    temp=len(a)
    print("Intersection  of texts: ",c)
    print("Union of texts: ",a.union(b))
    return float(len(c)) / (temp + len(b) - len(c))

# text1="Music is a universal feature of the human experience"
# text2="Music is a universal language"
# print("Cosine Similarity is: ",cosine_sim(text1,text2,"N"),"\n")
# print("Euclidean Similarity is: ",euclidean_sim(text1,text2),"\n")
# print("Jaccard Similarity is: ",jaccard_sim(text1,text2),"\n")