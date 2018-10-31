from string import ascii_lowercase

def is_pangram(sentence):

    abc = set(list(ascii_lowercase))
    pangramcheck = set(list(sentence.lower()))
    return abc.issubset(pangramcheck)
