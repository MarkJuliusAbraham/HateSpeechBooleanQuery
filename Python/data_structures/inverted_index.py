import queue
import os
import data_structures.postings as postingslist


class InvertedIndex:

    my_queue = None

    _inverted_index = None


    def __init__(self):
        self.my_queue = queue.Queue(maxsize=0)
        self._inverted_index = {}

    def add_term(self, term, docID):

        # if term is new, create a key of the term with the value of an empty postings.
        if term not in self._inverted_index:
            self._inverted_index[term] = postingslist.Postings() 

        # at this point, the term must already have a postings, and updating the postings is the only concern
        
        self._inverted_index[term].updatePostings(docID)

    def get_keys(self):
        return self._inverted_index.keys()

    def get_postings(self, term):
        return self._inverted_index[term]

    def __str__(self) -> str:
        inverted_index_string = ""

        for term in self._inverted_index.keys():
            inverted_index_string = inverted_index_string + " " + str(term) + ": " + str(self._inverted_index[term]) + "\n"

        inverted_index_string += ""

        return inverted_index_string

    def __repr__(self) -> str:
        pass
if __name__ == '__main__':
    
    os.system('cls' if os.name == 'nt' else 'clear')

    custom_queue = InvertedIndex()
    print(custom_queue)