import re

def count_words(sentence):
    count = {}
    sentence = sentence.strip("'").strip('"').replace("\n", " ").replace("_", " ")
    
    cleaned = re.split(r"[^\w']+", sentence.lower())
    for word in cleaned:
        word = word.strip("'")
        if word != '':
            if word in count:
                count[word] += 1
            else:
                count[word] = 1
    return count