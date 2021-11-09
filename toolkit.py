import os
import argparse
from numpy.core.einsumfunc import einsum
from similarities import cosine_sim, euclidean_sim, jaccard_sim
from preprocess import preprocess
import nltk
#nltk.download('punkt')
#nltk.download('stopwords')

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
    
def Sort(sub_li):
    sub_li.sort(key = lambda x: x[1])
    return sub_li

def stem():
    pass

def print_sim(sim_type,file1,file2,mode=""):
    print("File 1: ", file1)
    print("File 2: ", file2)
    sim = ""
    score = 0

    file1 = open(file1)
    file2 = open(file2)

    txt1 = file1.read()
    txt2 = file2.read()

    file1.close()
    file2.close()

    txt1 = preprocess(txt1)
    txt2 = preprocess(txt2)

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

def similar(args):
    sim_type = args.similar[0]
    dir_or_file = args.similar[1]

    mode = ""
    if sim_type in ['c','e']:
        mode = input("Enter mode")

    if dir_or_file == 0:  #directory
        dir_name = input("Enter dir name: ")
        if not check_dir(dir_name):
            print("Enter valid dir name")
            return
        file_list = get_files(dir_name)
        res_list = []

        for i in range(0,file_list.length()):
            for j in range(i+1,file_list.length()):
                file1 = file_list[i]
                file2 = file_list[2] 
                score = print_sim(sim_type,os.path.join(dir_name,file1),os.path.join(dir_name,file2),mode)
                res_list.append([file1+" "+file2,score])
        Sort(res_list)
        for val in Sort:
            print(val[0]+" : "+val[1])

    elif dir_or_file == 1:
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

        Sort(res_list)
        for val in Sort:
            print(val[0]+" : "+val[1])


        


def txtsearch():
    pass

def visualisefile():
    pass

def visualisedir():
    pass


if __name__ == "__main__":

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