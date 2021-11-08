import os
import argparse

def check_file(fname):
    return os.path.isfile(fname) 

def check_dir(dname):
    return os.path.isdir(dname) 
    

def preprocess():
    pass

def stem():
    pass

def similar():
    pass

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