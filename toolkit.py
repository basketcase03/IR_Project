import os
import argparse
from mid_funcs import *


#The main function called when script executed
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description = "Information Retrieval Toolkit")

    #Adding various arguments to the parser
    parser.add_argument("-p", "--stem", type = str, nargs = 1,
                        metavar = "file_name", 
                        help = "Outputs ans stores stemmed version of file in same dir.")
  
    parser.add_argument("-s", "--similar", type = str, nargs = 2,
                       metavar = ('sim_type','doc_or_file'),
                       help = "Shows similarity score btw files.\
                           c: cosine, (Furthermore types = B,T)\
                           e: euclidean, (Furthermore types = B,T) \
                           j: jaccard \
                            \
                           0: all in dir \
                           1: 2 files\
                           2: file and dir" )
      
    parser.add_argument("-t", "--txtsearch", type = str, nargs = 2,
                        metavar = ('txt','file1'), 
                        help = "Returns if text present in given document. \
                            Furthermore\
                           b:brute force\
                           k: KMP \
                           r: Rabin Karp ")

    
    parser.add_argument("-f", "--visualisefile", type = str, nargs = 2,
                        metavar = ('file1','file2'), 
                        help = "Visualisation of similarity scores\
                            Furthermore: \
                           c: cosine, (Furthermore types = B,T)\
                           e: euclidean, (Furthermore types = B,T) \
                           j: jaccard ")
  
    args = parser.parse_args()
      
    #Using the conditions to process the arguments supplied from CLI
    if args.stem != None:
        stem(args)
    if args.similar != None:
        similar(args)
    if args.txtsearch !=None:
        txtsearch(args)
    if args.visualisefile != None:
        visualisefile(args)
