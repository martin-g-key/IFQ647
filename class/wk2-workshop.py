"""
Module 2 workshop
"""


"""
Task 1.3 Document Frequency
document frequency counts how many different documents have at least one occurrence of that word

"""
docs = {'D1':{'term1':3, 'term4':5, 'term5':7},'D2':{'term1':5, 'term2':3, 'term3':4, 'term4':6}, 'D3':{'term3':5, 'term4':4, 'term5':6}, 'D4':{'term1':9, 'term4':1, 'term5':2}, 'D5':{'term2':1, 'term4':3, 'term5':2},'D6':{'term1':3, 'term3':2, 'term4':4, 'term5':4}}

def c_df(input): 
    doc_freq = {}

    for doc in docs:
        #print(doc, docs[doc])

        for k, v in docs[doc].items():
            #print(doc, k, v) 

            if k in doc_freq: 
                doc_freq[k] += 1
            else:
                doc_freq[k] = 1

    # sort by value 
    #doc_freq = dict(sorted(doc_freq.items(), key= lambda item: item[1]))

    # sort by key 
    doc_freq = dict(sorted(doc_freq.items(), key = None))

    return doc_freq 


def main():
    # print(c_df(docs)) # task 1.3
    pass

if __name__ == "__main__":
    main()