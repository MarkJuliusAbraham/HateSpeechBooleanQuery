import queue
import os

class CustomQueue:

    my_queue = None

    def __init__(self):
        self.my_queue = queue.Queue(maxsize=0)

    def enqueue(self, entry, term_frequency:int):
        self.my_queue.put([entry,term_frequency])
    
    def enqueue(self, entry):
        self.my_queue.put(entry)

    def dequeue(self):
        return self.my_queue.get()
    
    def strdequeue(self):
        return str(self.my_queue.get())

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

    custom_queue = CustomQueue()

    print(custom_queue)