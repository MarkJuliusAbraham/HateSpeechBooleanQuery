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

        self._inverted_index[term].display()

    def enqueue(self, entry):
        self.my_queue.put(entry)

    def dequeue(self):
        return self.my_queue.get()
    
    def strdequeue(self):
        return str(self.my_queue.get())

    def create_new_postings():
        pass

    def update_termfrqncy_at_(docID):
        pass
    
    def size(self):
        return self.my_queue.qsize()

    def __str__(self) -> str:
        
        temp_queue = queue.Queue(maxsize=(self.my_queue.qsize()))


        k = '['
        initial_size = self.my_queue.qsize()

        for i in range(initial_size):
            entry = self.my_queue.get()

            if((i+1) == initial_size):
                k = k + str(entry) + ']'
            else:
                k = k + str(entry) + ','
            temp_queue.put(entry) 

        self.my_queue = temp_queue

        return k
    
    def __repr__(self) -> str:
        
        temp_queue = queue.Queue(maxsize=(self.my_queue.qsize()))


        k = '['
        initial_size = self.my_queue.qsize()

        for i in range(initial_size):
            entry = self.my_queue.get()

            if((i+1) == initial_size):
                k = k + str(entry) + ']'
            else:
                k = k + str(entry) + ','
            temp_queue.put(entry) 

        self.my_queue = temp_queue

        return k

if __name__ == '__main__':
    
    os.system('cls' if os.name == 'nt' else 'clear')

    custom_queue = InvertedIndex()

    print(custom_queue)