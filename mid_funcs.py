from re import sub
from numpy.core.einsumfunc import einsum
from similarities import cosine_sim, euclidean_sim, jaccard_sim
from preprocess import preprocess
from stemming import stemming
import nltk
from plotting import plot
from txtsearch import KMP, RKarp, brute_force
import os
from pathlib import Path
#nltk.download('punkt')
#nltk.download('stopwords')

#To check if file exists
def check_file(fname):
    return os.path.isfile(fname) 

#To check if directory exists
def check_dir(dname):
    return os.path.isdir(dname) 

#Return files present in directory
def get_files(dir_name):
    file_list = []
    for file in os.listdir(dir_name):
        if file.endswith(".txt"):
            file_list.append(os.path.join(dir_name, file))
    return file_list
    
#Return preprocessed text of a file
def get_text(fname):
    file1 = open(fname)
    txt = file1.read()
    file1.close()
    txt = preprocess(txt)
    return txt

#Function to sort list in desc order
def Sort(sub_li):
    sub_li.sort(key = lambda x: x[1])
    sub_li.reverse()
    return sub_li

#Return stemmed text
def stem(args):
    fname = args.stem[0]
    if not check_file(fname):
        print("Enter valid file name")
        return
    stemmed = (stemming(get_text(fname)))
    print(stemmed)
    head, n_file = os.path.split(fname)
    n_file = Path(fname).stem
    n_file = n_file + "stem.txt"
    n_file = os.path.join(head,n_file)
    with open(n_file, 'w') as f:
        f.write(stemmed)

#Return similarity score
def print_sim(sim_type,file1,file2,mode=""):
    print("File 1: ", file1)
    print("File 2: ", file2)
    sim = ""
    score = 0

    txt1 = get_text(file1)
    txt2 = get_text(file2)

    if sim_type == 'c':
        sim = "cosine"
        score = cosine_sim(txt1,txt2,mode)
    elif sim_type == 'e':
        sim = "euclidean"
        score = euclidean_sim(txt1,txt2,mode)
    else:
        sim = "jaccard"
        score = jaccard_sim(txt1,txt2)
    print("Similarity score ({sim_}) is : {score_}".format(sim_=sim,score_=score))
    return score

#Process the similarity
def similar(args):
    sim_type = args.similar[0]
    dir_or_file = args.similar[1]

    mode = ""
    if sim_type in ['c','e']:
        mode = input("Enter mode")

    if dir_or_file == '0':  #directory
        dir_name = input("Enter dir name: ")
        if not check_dir(dir_name):
            print("Enter valid dir name")
            return
        file_list = get_files(dir_name)
        res_list = []

        for i in range(0,len(file_list)):
            for j in range(i+1,len(file_list)):
                file1 = file_list[i]
                file2 = file_list[j] 
                score = print_sim(sim_type,os.path.join(dir_name,file1),os.path.join(dir_name,file2),mode)
                res_list.append([file1+" "+file2,score])
        res_list = Sort(res_list)
        for val in res_list:
            print(val[0]+" : "+str(val[1]))

    elif dir_or_file == '1':
        file1 = input("Enter file1: ")
        file2 = input("Enter file2: ")
        if (not check_file(file1)) or (not check_file(file2)):
            print("Enter valid file name")
            return 
        print_sim(sim_type,file1,file2,mode)

    else:
        file1 = input("Enter file: ")
        dir_name = input("Enter dir: ")

        if (not check_file(file1)) or (not check_dir(dir_name)):
            print("Enter valid path")
            return
        
        file_list = get_files(dir_name)
        res_list = []

        for file2 in file_list:
            if file1 == file2:
                continue
            score = print_sim(sim_type,os.path.join(dir_name,file1),os.path.join(dir_name,file2),mode)
            res_list.append([file1+" "+file2,score])

        res_list = Sort(res_list)
        for val in res_list:
            print(val[0]+" : "+str(val[1]))

#Return text search
def txtsearch(args):
    pat = args.txtsearch[0]
    txt = get_text(args.txtsearch[1])
    search_type = input("Enter algo to search with : ")
    if search_type == 'b':
        print("Position: ",brute_force(pat,txt))
    elif search_type == 'k':
        print("Position: ",KMP(pat,txt))
    else:
        print("Position:",RKarp(pat,txt))

#Function to visualise similarity score
def visualisefile(args):
    file1 = args.visualisefile[0]
    file2 = args.visualisefile[1]
    txt1 = Path(args.visualisefile[0]).stem
    txt2 = Path(args.visualisefile[1]).stem
    sim_type = input("Enter type of similarity: ")
    mode = "B"
    score = print_sim(sim_type,file1,file2,mode)
    plot(score,txt1,txt2)
