import sys
from stats import word_count
from stats import char_count
from stats import output_list

#validate path passed by sys module and set the provided path attribute to contents variable
filepath = ""
if len(sys.argv) < 2:
    print(f"Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    filepath = sys.argv[1]

# takes filepath and returns contents as a string
def get_book_text(filepath_in):
    try:
        with open(filepath_in, 'r') as f:
            file_contents = f.read()
            return file_contents
    except FileNotFoundError:
        print(f"Error: File not found at '{filepath_in}'")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

from stats import word_count
from stats import char_count
from stats import output_list

def main():
    contents = "my_file.txt"
    num_words = 0
    char_dict = {}
    out_list = []
    contents = get_book_text(filepath)
    num_words = word_count(contents)
    char_dict = char_count(contents)
    out_list =  output_list(char_dict)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dictionary in out_list:
            if dictionary["char"].isalpha():
                print(f"{dictionary["char"]}: {dictionary["num"]}") 

    # print(output_list(char_dict))
    print("============= END ===============")

main()