import string
import sys

def count_unique_word():
    words = {}
    strip = string.whitespace + string.punctuation + string.digits + "\"'"
    with open(filename, encoding='UTF-8') as file:        
        for line in file:
            for word in line.lower().split():
                word = word.strip(strip)
                words[word] = words.setdefault(word, 0) + 1

    return words

def majorityCnt(words):
    a=sorted(words.items(),key=lambda x:x[1], reverse=True)
    return a[0]

