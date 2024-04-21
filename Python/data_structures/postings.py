import queue

class Postings:

    keys = None
    my_queue = None

    def __init__(self):
        self.my_queue = queue.Queue(maxsize=0)
        self.keys = {}

    def updatePostings(self, docID):
        
        if docID not in self.keys:
            self.keys[docID] = 0
            self.my_queue.put(docID)
        self.keys[docID] += 1

    def display(self):
        print(self.keys)
        print(self.my_queue)