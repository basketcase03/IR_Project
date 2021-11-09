import os
import argparse
from numpy.core.einsumfunc import einsum
from similarities import cosine_sim, euclidean_sim, jaccard_sim
from preprocess import preprocess

def check_file(fname):
    return os.path.isfile(fname) 

def check_dir(dname):
    return os.path.isdir(dname) 

def get_files(dir_name):
    file_list = []
    for myfile in os.listdir(dir_name):
        if file.endswith(".txt"):
            file_list.append(os.path.join(dir_name, myfile))
    return file_list
    

def stem():
    pass

def print_sim(sim_type,file1,file2):
    print("File 1: ".file1)
    print("File 2: "file2,)
    sim = ""
    score = 0

    txt1 = file1.read()
    txt2 = file2.read()

    txt1 = preprocess(txt1)
    txt2 = preprocess(txt2)

    if sim_type == 'c':
        sim = "cosine"
        score = cosine_sim(txt1,txt2)
    elif sim_type == 'e':
        sim = "euclidean"
        score = euclidean_sim(txt1,txt2)
    else:
        sim = "jaccard"
        score = jaccard_sim(txt1,txt2)
    print("Similarity score (sim_} is : {score_}".format(sim_=sim,score_=score))

def similar(args):
     c: cosine \
                           e: euclidean \
                           j: jaccard \
                            \
                           0: dir \
                           1: files")


    sim_type = args.similar[0]
    dir_or_file = args.similar[1]

    if dir_or_file == 0:  #directory
        dir_name = input("Enter dir name: ")
        if not check_dir(dir_name):
            print("Enter valid dir name")
            return
        file_list = get_files(dir_name)
        for file1 in file_list:
            for file2 in file_list:
                print_sim(sim_type,file1,file2)
    else:
        file1 = input("Enter file1: ")
        file2 = input("Enter file2: ")
        if (not check_file(file1)) or (not check_file(file2)):
            print("Enter valid file name")
            return 
        print_sim(sim_type,file1,file2)

def txtsearch():
    pass

def visualisefile():
    pass

def visualisedir():
    pass

def main():

    parser = argparse.ArgumentParser(description = "Information Retrieval Toolkit")

    parser.add_argument("-p", "--stem", type = str, nargs = 1,
                        metavar = "file_name", 
                        help = "Stores stemmed version of file in same dir.")
  
    parser.add_argument("-s", "--similar", type = str, nargs = 2,
                       metavar = ('sim_type','doc_or_file'),
                       help = "Shows similarity score btw files.\
                           c: cosine \
                           e: euclidean \
                           j: jaccard \
                            \
                           0: dir \
                           1: files")
      
    parser.add_argument("-t", "--txtsearch", type = str, nargs = 2,
                        metavar = ('txt','file1'), 
                        help = "Returns if text present in given document.")
    
    parser.add_argument("-f", "--visualisefile", type = str, nargs = 1,
                        metavar = 'file_name',
                        help = "Saves visualisations of n-grams.")

    parser.add_argument("-d", "--visualisedir", type = str, nargs = 1,
                        metavar = 'dir_name',
                        help = "Saves visualisations of similarity scores.")
  
    args = parser.parse_args()
      
    if args.stem != None:
        stem(args)
    if args.similar != None:
        similar(args)
    if args.txtsearch !=None:
        txtsearch(args)
    if args.visualisefile != None:
        visualisefile(args)
    if args.visualisedir != None:
        visualisedir(args)