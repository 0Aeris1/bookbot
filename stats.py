
def get_book_text(filepath):
    with open(filepath) as b:
        file_contents = b.read()
    return str(file_contents)

def word_count(text):
    return f"Found {len(text.split())} total words"

def character_count(text):
    chars = {}
    for char in text.lower():
        chars[char] = chars.get(char, 0) + 1
    return chars


def sorted_list_chars(chars):
    char_list = []
    for char, count in chars.items():
        if char.isalpha():
            char_list.append({"char": char, "count": count}) 
            
    def help_sort(char_list):
        return char_list["count"]
    char_list.sort(key=help_sort, reverse=True)
    
    return char_list

    
    
