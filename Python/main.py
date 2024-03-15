import index
import index.index_tools as indt
import index.constants as constants


def main():
    
    warning()

    my_indexer = indt.Indexer(constants.PATH_TO_SMALL_JSON, constants.PATH_TO_INVERTED_INDEX)
    my_indexer.create_inverted_index()
    # my_index.check_initialization()



def warning():
    
    print("\n---------------------")
    print("\nPython script was executed using main.py.")
    print("\n---------------------\n\n")

if __name__ == "__main__":
    main()