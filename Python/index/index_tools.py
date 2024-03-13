import json

class Indexer:

    _dataset = None

    def __init__(self, dataset) -> None:
        """Initialize Indexer with the given attribute.

        Args:
            dataset (string): A string representing the filepath to the labeled json file that is to be indexed.
        """

        # Open the JSON file for reading
        with open(dataset, 'r') as file:
            # Load the JSON data from the file
            self._dataset = json.load(file)


    def print_dataset(self):
        print('\n')
        for item in self._dataset:
            print(item)
            print('\n')

if __name__ == "__main__":
    
    my_index = Indexer('./Dataset/Subset/subset_labeled_data.json')
    my_index.print_dataset()