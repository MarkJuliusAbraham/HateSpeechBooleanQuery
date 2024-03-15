import json
import os

import index.constants as constants
import data_structures.custom_queue as queue

class Indexer:

    _inverted_index_path = None
    _inverted_index = {}
    _dataset_path = None
    _dataset = None

    def __init__(self, dataset_path: str, inverted_index_path: str) -> None:
        """Initialize Indexer with the given attribute.

        Args:
            dataset_path (string): A string representing the filepath to the labeled json file that is to be indexed.
        """

        self._dataset_path = dataset_path
        self._inverted_index_path = inverted_index_path

        # Open the JSON file for reading
        with open(dataset_path, 'r') as file:
            # Load the JSON data from the file
            self._dataset = json.load(file)

        k = 1
        for item in self._dataset:
            item[constants.DOCID] = k
            k+=1

    def _create_empty_inverted_index(self):
        """
            Creates an boilerplate text file determined and located by self._inverted_index_path
        """

        with open(self._inverted_index_path, 'w') as file:
            # Write data to the file
            file.write('Hello, world!\n')
            file.write('This is a test.\n')
            file.write('Writing to a file in Python.\n')

    def create_inverted_index(self):
        """Creates the Inverted Index determined and located by self._inverted_index_path.
        """
        
        for entry in self._dataset:
            for word in (entry[constants.TWEET].split(' ')):
                if word not in self._inverted_index: #first time the word occurs
                    self._inverted_index[word] = queue.CustomQueue()
                    self._inverted_index[word].enqueue(entry[constants.DOCID])
                else:
                    self._inverted_index[word].enqueue(entry[constants.DOCID])
                    pass
        
        print(self._inverted_index)

    def check_initialization(self):

        print("Labeled Data used at path: " + self._dataset_path + "\n")
        print("Inverted Index created at path:" + self._inverted_index_path + "\n")
        print("-------------------------------------------------------")
        print("Initialized list from json is listed as follows: \n")
        for item in self._dataset:
            print(item)
            print('\n')

def warning():
    
    print("\n---------------------")
    print("\nPython script was executed using index_tools.py.")
    print("\n---------------------\n\n")



if __name__ == "__main__":

    os.system('cls' if os.name == 'nt' else 'clear')
    warning()
    
    my_index = Indexer(constants.PATH_TO_SMALL_JSON,constants.PATH_TO_INVERTED_INDEX)