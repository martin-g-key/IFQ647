"""
IFQ647 ML for NLP
Task 1.1 --> define Parse_Docs function
Task 1.2 --> define Parse_Q function
Task 1.3 --> define main function
"""

"""
Task 1.1 
"""
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
        return self.news_id

    @newsID.setter
    def newsID(self )

    def getTermsList():
        pass
    
    # use bag of words for each document


def Parse_Docs(
        stop_words ="a1/data/IFQ647_asm1_data/common-english-words.txt", 
        input_folder ="a1/data/IFQ647_asm1_data/RCV1v3"
    ):
    # read the xml files from inputfolder

    with open(input_folder, "r", encoding="utf-8") as f:

        f_ = f.readlines()
        start_end=False
        news = "" # blank string to add text to 
        word_count = 0 

        for line in f_:
            line = line.strip()
            if (start_end == False): 
                if line.startswith("<newsitem "): 
                    for part in line.split():
                        if part.startswith("itemid="):
                            docid = part.split("=")[1].split("\"")[1]
                            break 
                if line.startswith("<text>"):
                    start_end=True 
            elif line.startswith("</text>"):
                break
            else:
                # remove paragraph tags
                line = line.replace("<p>", "").replace("</p>", "")
                news = news + line + "\n"
                for term in line.split():
                    word_count += 1 

    f.close 

    

