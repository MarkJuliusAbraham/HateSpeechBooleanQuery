import index.index_tools as indt

def main():
    
    warning()

    my_index = indt.Indexer('./Dataset/Subset/subset_labeled_data.json')
    my_index.print_dataset()


def warning():
    
    print("\n---------------------")
    print("\nPython script was executed using main.py.")
    print("\n---------------------\n\n")

if __name__ == "__main__":
    main()