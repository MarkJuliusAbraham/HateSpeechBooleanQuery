import index
import os
import index.index_machine as indt
import index.constants as constants


def main():
    
    warning()

    my_indexer = indt.IndexMachine(constants.PATH_TO_LABELED_JSON, constants.PATH_TO_INVERTED_INDEX)
    my_indexer.create_inverted_index()

def warning():
    
    print("\n---------------------")
    print("\nPython script was executed using main.py.")
    print("\n---------------------\n\n")

if __name__ == "__main__":
    
    os.system('cls' if os.name == 'nt' else 'clear')
    main()