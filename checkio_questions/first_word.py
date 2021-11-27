'''
solution 1
'''
def first_word(text):
    text = text.replace('.', ' ').replace(',', ' ').strip()
    text = text.split()
    return text[0]


'''
solution 2
'''
import re
def first_word(text: str) -> str:
    return re.search("([\w']+)", text).group(1)
    # () capture and group
    # [] A set of characters
    # \ Signals a special sequence --> \w Returns a match where the string contains any word character
    # + one or more occurunce 
    # .group() returns the part of the string where there was a match

'''
solution3
''' 
def first_word(text: str) -> str:
    i = 0
    while i < len(text) and text[i] in ',. ':
        i += 1
    j = i
    while j < len(text) and text[j] not in ',. ':
        j += 1
    return text[i:j]

if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")
