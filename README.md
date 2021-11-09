# IR_Project
Project for information retrieval 

Python CLI 
1. Get similarity scores
2. Get text search
3. Apply stemming on a document
4. Visualise score

## Usage
1. Clone the project.
2. Enter the directory and execute the script.
3. Use python3 toolkit.py -h  : for help

Examples:

python3 toolkit.py -s c 0
Cosine similarity of whole doc

python3 toolkit.py -s e 3
Euclidean similarity of a file with a directory

python3 toolkit.py -t apple IR_Project/IR_Project/test_dir/txt2.txt
Search the pattern "apple" in given file

python3 toolkit.py -p IR_Project/IR_Project/txt1.txt
Apply stemming on the given doc

python3 toolkit.py -f IR_Project/IR_Project/txt1.txt IR_Project/IR_Project/txt2.txt
Visualise similiarty scores of given docs
