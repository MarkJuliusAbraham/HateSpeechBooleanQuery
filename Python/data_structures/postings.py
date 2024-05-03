import queue

class Postings:

    keys = None
    my_queue = None

    def __init__(self):
        self.my_queue = queue.Queue(maxsize=0)
        self.keys = {}

    def updatePostings(self, docID):
        
        if docID not in self.docIDsInPostingsList():
            self.addDocIDtoPostingsList(docID)
        
        self.incrementDocumentFrequency(docID)

    def display(self):
        print(self.keys)
        print(self.my_queue)

    def docIDsInPostingsList(self):
        return self.keys
    
    def addDocIDtoPostingsList(self,docID):
        self.keys[docID] = 0
        self.my_queue.put(docID)

    def incrementDocumentFrequency(self, docID):
        self.keys[docID] += 1 

    def get_postings_size(self):
        return len(self.keys)
    
    def dequeue(self):
        return self.my_queue.get()

    def get_doc_freq(self, docID):
        return self.keys[docID]

    def __str__(self) -> str:
        
        postings_as_string = ""

        for key in self.docIDsInPostingsList().keys():
            postings_as_string = postings_as_string + " " + str(key) + ":" + str(self.keys[key])

        postings_as_string += " "
        return postings_as_string
    
    def __repr__(self) -> str:
        
        return self.__str__
    

if __name__ == '__main__':
    
    

    custom_queue = Postings()
    custom_queue.updatePostings(2)
    custom_queue.updatePostings(2)
    custom_queue.updatePostings(3)
    custom_queue.updatePostings(9)
    custom_queue.updatePostings(9)
    custom_queue.updatePostings(10)
    custom_queue.updatePostings(10)
    custom_queue.updatePostings(11)
    
    print(custom_queue.get_postings_size())

    print(custom_queue)