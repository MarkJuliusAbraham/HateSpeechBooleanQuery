import json
import os

import index.constants as constants

import data_structures.inverted_index as inverted_index

class IndexMachine:

    _inverted_index_path = None
    _inverted_index = None
    _dataset_path = None
    _dataset = None

    def __init__(self, dataset_path: str, inverted_index_path: str) -> None:
        """Initialize Indexer with the given attribute.

        Args:
            dataset_path (string): A string representing the filepath to the labeled json file that is to be indexed.
        """

        self._dataset_path = dataset_path
        self._inverted_index_path = inverted_index_path
        self._inverted_index = inverted_index.InvertedIndex()

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

        with open(self._inverted_index_path, 'w') as file:

            for entry in self._dataset:
                # for each word in the entry or line of the tweet, split by the ' ':
                for word in (entry[constants.TWEET].split(' ')):

                    term = word.lower()

                    self._inverted_index.add_term(term, entry[constants.DOCID])
    
        self.write_inverted_index_to_file(self._inverted_index, self._inverted_index_path)


    # def create_inverted_index(self):
    #     """Creates the Inverted Index determined and located by self._inverted_index_path.
    #     """

    #     # note that self._dataset is a json object
    #     # and self._inverted_index is simply a disctionary with terms as keys and postings ( created using custom queues) as values
        
    #     with open(self._inverted_index_path, 'w') as file:

    #         for entry in self._dataset:
    #             # for each word in the entry or line of the tweet, split by the ' ':
    #             for word in (entry[constants.TWEET].split(' ')):

    #                 term = word.lower()

    #                 if term not in self._inverted_index: #first time the word occurs

    #                     # place a custom queue as a value, using the word as a key. 
    #                     # this custom queue represents the postings list
    #                     self._inverted_index[term] = queue.InvertedIndex()
    #                     self._inverted_index[term].enqueue(entry[constants.DOCID])


    #                 else:   # occurs only if the word is already a valid key

    #                     # since the key is valid, then there exists already a custom queue as value that can be accessed
    #                     # enqueue the DOCID value
    #                     self._inverted_index[term].enqueue(entry[constants.DOCID]) 
    
    #     self.write_inverted_index_to_file(self._inverted_index, self._inverted_index_path)

    def write_inverted_index_to_file(self, inverted_index, inverted_index_path):
        """
            A class method meant to be used for the self._inverted_index variable in the class.
            It reads the COMPLETED inverted index in memory and transcribes it to a tsv file.        

            Args:
                inverted_index (dictionary of the form {"string": "custom_queue object"})
                    see custom_queue.py in data_structures.
        """
        # print(self._inverted_index)

        keys_sorted = []

        for keys in inverted_index.get_keys():
            keys_sorted.append(keys)

        keys_sorted.sort()

        with open(inverted_index_path, 'w') as file:
            for key in keys_sorted:
                file.write(key)
                file.write('\t')

                posting_size = inverted_index.get_postings(key).get_postings_size()
                file.write(str(posting_size))
                file.write('\t')

                for count in range(posting_size):
                    current_postings = inverted_index.get_postings(key)
                    current_docID = current_postings.dequeue()
                    file.write(str(current_docID))
                    file.write('\t')
                    file.write(str(current_postings.get_doc_freq(current_docID)))
                    file.write('\t')
                file.write('\n')

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

if __name__ != "__main__":

    os.system('cls' if os.name == 'nt' else 'clear')
    warning()
    
    