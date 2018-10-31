import re

def hey(phrase):
    a = "Whoa, chill out!"
    b = "Whatever."
    c = "Sure."
    d = "Calm down, I know what I'm doing!"
    e = "Fine. Be that way!"

    phrase = phrase.strip()
    pattern = re.compile(r'[A-Z]+')
    p = pattern.search(phrase)

    if phrase == "":
        return e

    elif phrase == phrase.upper() and p :

        if phrase[-1] == "?" :
            return d
        else:
            return a

    elif phrase[-1] == "?":
        return c

    else:
        return b