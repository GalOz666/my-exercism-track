from typing import List

def find_anagrams(word: str, candidates: List[str]):
    word_stripped = sorted(word.lower())
    enum_candidates = enumerate([y.lower() for y in candidates if y.lower() != word.lower()])

    possibles = [x[0] for x in enum_candidates if sorted(x[1]) == word_stripped]

    if possibles == []:
        return possibles

    else:
        return ([candidates[x] for x in possibles])

