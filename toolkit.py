def main():

    parser = argparse.ArgumentParser(description = "Information Retrieval Toolkit")

    parser.add_argument("-p", "--stem", type = str, nargs = 1,
                        metavar = "file_name", 
                        help = "Stores stemmed version of file in same dir.")
  
    parser.add_argument("-c", "--similar", type = str, nargs = 2,
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
    
    parser.add_argument("-v", "--visualisefile", type = str, nargs = 1,
                        metavar = 'file_name',
                        help = "Saves visualisations of n-grams.")

    parser.add_argument("-v", "--visualisedir", type = str, nargs = 1,
                        metavar = 'dir_name',
                        help = "Saves visualisations of similarity scores.")
  
    args = parser.parse_args()
      
    # calling functions depending on type of argument
    if args.stem != None:
        stem(args)
    if args.similar != None:
        similar(args)
    if args.txtsearch !=None:
        txtsearch(args)
    if args.alldir != None:
        alldir(args)
    if args.visualisefile != None:
        visualisefile(args)
    if args.visualisedir != None:
        visualisedir(args)