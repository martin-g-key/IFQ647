
"""
IFQ647 ML for NLP
Task 1.1 --> define Parse_Docs function
Task 1.2 --> define Parse_Q function
Task 1.3 --> define main function
"""

"""
Task 1.1.1

DocV3 class: 1 object per document
Attributes:
* newsID == item id in the xml files
* terms dictionary containing term and frequency as k:v pairs
* doc_size


Methods:

"""


import pathLib 


# define docv3 class 
class DocV3():

    # constructor 
    def __init__(
        self,
        newsID = "",
        terms = {},
        size = 0 
    ):
        self.newsID = newsID
        self.terms = terms
        self.size = size 

    @property 
    def newsID(self):
        return self.newsID

    @newsID.setter
    def set_newsID(self):
        print("Placeholder newsID setter")

    @property
    def terms(self): 
        return self.terms

    @terms.setter
    def set_terms(self):
        print("Placeholder: terms setter")
        ## key, value = term, doc_size

    @property
    def doc_size(self):
        return self.doc_size

    @doc_size.setter
    def set_doc_size(self):
        print("placeholder: doc_size setter")




"""
    ## iterate through folder
    folder = Path(input_folder)
    for item in folder.iterdir():
        if item.is_file():

            ## iterate through file
            file = open(item, "r") 
            start_end = False
            file_ = file.readlines()
            word_count = 0
            for line in file_:
                line = line.strip()
                if start_end == False: 
                    if line.startswith("<newsitem "):
                        for part in line.split():
                            if part.startswith("itemid="):
                                docid = part.split("=")[1].split("\"")[1]
                                break
                    if line.startswith("<text>"):
                        start_end = True
                elif line.startswith("</text>"):
                    break
                else:
                    line = line.replace("<p>", "").replace("</p>", "")
                    line = line.translate(str.maketrans('','', string.digits)).translate(str.maketrans(string.punctuation, ' '*len(string.punctuation)))
                    for term in line.split():
                        word_count += 1
            # close file 
            file.close()                    
            
            return file.name, docid, word_count
        else:
            print(f"f{file} is not a file.")


    
    ## tokenising
    ## stop word removal
    ## stemming

    return Rcv1Coll
"""
