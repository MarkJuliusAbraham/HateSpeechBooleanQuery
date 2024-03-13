import index.index_tools as indt
import index.constants as constants

def main():
    
    warning()

    my_index = indt.Indexer(constants.PATH_TO_LABELED_JSON, constants.PATH_TO_INVERTED_INDEX)
    my_index.check_initialization()



def warning():
    
    print("\n---------------------")
    print("\nPython script was executed using main.py.")
    print("\n---------------------\n\n")

if __name__ == "__main__":
    main()