from collections import Counter
import re

# doesn't preserve order of discovery but is much faster and elegant
def word_count(phrase: str) -> dict[str : int]:
    parsed = re.sub(r'[^A-Za-z\']',' ', phrase)
    word_list = [x.strip('\'') for x in parsed.strip().lower().split()]
    return Counter(word_list)

# This passes all the tests but is less elegant in my opinion
def defaultdict_count(phrase: str) -> dict[str : int]:
    parsed = re.sub(r'[^A-Za-z\']',' ', phrase)
    word_list = [x.strip('\'') for x in parsed.strip().lower().split()]

    counter = {}

    for word in word_list:
        counter.setdefault(word, 0)
        counter[word] = counter[word]+1

    return counter


