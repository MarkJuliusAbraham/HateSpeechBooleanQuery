import json
import constants

class Indexer:


    _inverted_index_path = None
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

    def check_initialization(self):

        print("Labeled Data used at path: " + self._dataset_path + "\n")
        print("Inverted Index created at path:" + self._inverted_index_path + "\n")
        print("-------------------------------------------------------")
        print("Initialized list from json is listed as follows: \n")
        for item in self._dataset:
            print(item)
            print('\n')

if __name__ == "__main__":
    
    my_index = Indexer(constants.PATH_TO_LABELED_JSON,constants.PATH_TO_INVERTED_INDEX)
    my_index.create_inverted_index()