def count_words(file_contents):
    file_contents = file_contents.split() #splits the string into a list of words
    num_words = len(file_contents)  #counts the number of words in the list
    return num_words

def count_char(file_contents):
    file_contents = file_contents.lower()
    char_dict = {}
    for char in file_contents:
        if char.isalpha():  # Check if the character is a letter
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

def sorted_report(char_dict):
    sorted_chars = sorted(char_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_chars