import pandas as pd
import numpy as np
from math import sqrt
from sklearn.preprocessing import normalize
from sklearn.feature_extraction.text import CountVectorizer


## -------------------------------Function to calculate binary term frequencies----------------------------------------
def calculate_count_matrix(document):     
    cv=CountVectorizer()
    cv.fit(document)
    print("\nVocabulary: ", cv.vocabulary_)
    count_matrix = cv.transform(document)

    count_matrix = pd.DataFrame(count_matrix.toarray(), columns=cv.get_feature_names())
    print("\nEncoded Document is:")
    print(count_matrix)
    return count_matrix

## -------------------------------Function to calculate tf-idf of given documents----------------------------------------
def calculate_tf_idf(documents):    
    #Caculating term frequency                          
    data = pd.DataFrame(documents,columns=['Document text'])
    count_matrix=calculate_count_matrix(data['Document text'])

    #Caculating document frequency 
    df=np.array(count_matrix.astype(bool).sum())
    print("\nDocument frequency Matrix\n",df)
    n_samples=len(documents)

    #Calculating Inverse document frequency
    flag=True
    df+=int(flag)
    n_samples+=int(flag)
    idf=np.log(n_samples/df)+1
    print("\nInverse Document frequency\n",idf)

    #Normalising tf-idf
    df_before_normalization = count_matrix*idf
    tf_idf = normalize(df_before_normalization, norm='l2', axis=1)
    print("\ntf-idf Matrix\n",tf_idf)
    return tf_idf

## -------------------------------Function to calculate cosine similarity----------------------------------------
def cosine_sim(text1,text2,mode):
    document=[text1,text2]
    # If mode is binary, using binary matrix
    if mode=='B':
        count_matrix=calculate_count_matrix(document)
        count_matrix=count_matrix.to_numpy()
        count_matrix=normalize(count_matrix, norm='l2', axis=1)
    
        # #Caculating cosine similarity
        cos_sim=0
        for i in range(len(count_matrix[0])):
            cos_sim+= count_matrix[0][i]*count_matrix[1][i]
        return cos_sim

    # If mode is tf-idf, using tf-idf matrix
    elif mode=='T':
        count_matrix = calculate_tf_idf(document)
        #Caculating cosine similarity

        cos_sim=0
        for i in range(len(count_matrix[0])):
            cos_sim+= count_matrix[0][i]*count_matrix[1][i]
        return cos_sim

    else:
        print("Invalid Mode")
        return 0
    
    
    
## -------------------------------Function to calculate euclidean similarity----------------------------------------
def euclidean_sim(text1,text2,mode):
    document=[text1,text2]

    # If mode is binary, using binary matrix
    if mode=='B':
        count_matrix=calculate_count_matrix(document)
        count_matrix=count_matrix.to_numpy()
        count_matrix=normalize(count_matrix, norm='l2', axis=1)
    
        # #Caculating euclidean similarity
        euclid_sim=0
        for i in range(len(count_matrix[0])):
            euclid_sim+= (count_matrix[0][i]-count_matrix[1][i])**2
        return sqrt(euclid_sim)

    # If mode is tf-idf, using tf-idf matrix
    elif mode=='T':
        count_matrix = calculate_tf_idf(document)
        
        #Caculating euclidean similarity
        euclid_sim=0
        for i in range(len(count_matrix[0])):
            euclid_sim+= (count_matrix[0][i]-count_matrix[1][i])**2
        return sqrt(euclid_sim)

    else:
        print("Invalid Mode")
        return 0


## -------------------------------Function to calculate jaccard similarity----------------------------------------
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
# print("Cosine Similarity is: ",cosine_sim(text1,text2,"T"),"\n")
# print("Euclidean Similarity is: ",euclidean_sim(text1,text2,"T"),"\n")
# print("Jaccard Similarity is: ",jaccard_sim(text1,text2),"\n")
