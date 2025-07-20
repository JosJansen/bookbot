def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    text = text.lower()
    letter_count = {}

    for letter in text:
        if letter in letter_count:
            letter_count[letter] +=1
        else:
            letter_count[letter]=1
    
    return letter_count

def sort_on(items):
    return items["num"]

def sort_characters(text):
    list_text = []

    for letter in text:
        if letter.isalpha():
            list_text.append({"char":letter, "num":text[letter]})

    list_text.sort(reverse=True, key=sort_on)

    return list_text