# to do: fix paths for input and stops
# use class


import os
import string
from stemming.porter2 import stem 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data", "IFQ647_asm1_data")


class DocV3():

    # constructor 
    def __init__(
        self,
        newsID = "",
        terms = {},
        doc_size = 0 
    ):
        self.newsID = newsID
        self.terms = terms
        self.doc_size = doc_size 

    def get_newsID(self):
        return self.newsID

    def get_terms(self):
        return self.terms

    def get_doc_size(self):
        return self.doc_size

    def __str__(self):
        return f"{self.newsID}: {self.doc_size} terms"

class Rcv1Coll:
    def __init__(self):
        self._docs= {}

    def add(self, doc):
        if not isinstance(doc, DocV3):
            raise TypeError("Only DocV3's are allowed")
        else:
            self._docs[doc.newsID] = doc

    def __len__(self):
        return len(self._docs)

    def __iter__(self):
        return iter(self._docs)

    def __str__(self):
        return f"{len(self._docs)} documents in dictionary"


def Parse_Docs(input_folder, stop_words):
    stop_words = os.path.join(DATA_DIR, stop_words)
    input_folder = os.path.join(DATA_DIR, input_folder)  

    collection = Rcv1Coll()

    ## get a stop words list
    sw = open(stop_words)
    sw_list = sw.read().split(",")
    sw.close()
    
    ## iterate through files in folder 
    for item in os.listdir(input_folder):
        file = open(os.path.join(input_folder,item), "r")
        start_end = False
        current_doc = {}

        ## iterate through lines in file
        file_ = file.readlines()
        word_count = 0

        for line in file_:
            line = line.strip()
            if (start_end == False):
                if line.startswith("<newsitem "):
                    for part in line.split():
                        if part.startswith("itemid="):
                            docid = part.strip('"')
                            break
                if line.startswith("<text>"):
                    start_end = True
            elif line.startswith("</text>"):
                break
            else:
                line = line.replace("<p>","").replace("</p>","")
                line = line.translate(str.maketrans('', '', string.digits)).translate(str.maketrans(string.punctuation, ' '*len(string.punctuation)))
                for term in line.split():
                    word_count += 1
                    term = term.lower()
                    term = stem(term)
                    if len(term) > 2 and term not in sw_list:
                        try:
                            current_doc[term] += 1
                        except KeyError:
                            current_doc[term] = 1

        file.close()

        collection.add(DocV3(docid, current_doc, word_count))

    return collection


stop_words = "common-english-words.txt"
input_folder = "RCV1v3" 

c = Parse_Docs(input_folder,stop_words)


print(c)