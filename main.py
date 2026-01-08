import sys
from stats import get_book_text, word_count, character_count, sorted_list_chars

def main():

    if len(sys.argv) == 2:  
        read_book = get_book_text(sys.argv[1]) 
        print(word_count(read_book))
    else:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)        
    
    output = sorted_list_chars((character_count(read_book)))
    for item in output:
        print(f"{item['char']}: {item['count']}")

    
if __name__ == "__main__":
    main()


