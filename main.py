def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    lowered_text = text.lower()
    dictionary = get_chars_dict(lowered_text)

    print_chars_dict(dictionary)

def get_chars_dict(text):
    dictionary = {}
    for char in text:
        if char not in dictionary:
            dictionary[char] = 1
            continue
        
        dictionary[char] += 1
    
    return dictionary

def print_chars_dict(dictionary):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{sum(dictionary.values())} words found in the document \n")

    for key in dictionary:
        print(f"The '{key}' character was found {dictionary[key]} times")
    
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()