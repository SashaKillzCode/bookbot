def word_count(string_in):
    count = 0
    s = ""
    s = string_in
    count = len(s.split())
    return count

def char_count(string_in):
    s = ""
    char_counts = {}
    #create lower case version of string
    s = string_in.lower()
    for char in s:
        if char in char_counts:
            char_counts[char] += 1  # Increment count if character exists
        else:
            char_counts[char] = 1  # Add character with count 1 if it's new
    return char_counts

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(items):
    return items["num"]

def output_list(dict_in):
    sorted_list = []
    dict_out = {}
    for k in dict_in:
        sorted_list.append({"char":k,"num":dict_in[k]})
        
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list