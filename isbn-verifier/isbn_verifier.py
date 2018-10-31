import random, re

def verify(isbn: str, isbn_base=11) -> bool:

    isbn_s = isbn.lower().replace('-', '') #strip comas if needed

    #Sanity checks

    char_check = re.findall(r'[a-wyz]', isbn_s)
    if char_check != []:
        return False

    if len(isbn_s) != (isbn_base-1):
        return False

    if 'x' in isbn_s and isbn_s[-1] !='x':
        return False

    # parsing and reversing
    if 'x' in isbn_s:
        # transform x into 10 if needed
        parsed = isbn_s.replace('x', '')
        num_list = reversed([int(x) for x in parsed]+[10])
    else:
        num_list = reversed([int(x) for x in isbn_s])

    # multiplication by inverse index count

    multilist = [(x[0]+1)*x[1] for x in enumerate(num_list)]

    # for debugging
    # print((sum(multilist)%isbn_base) == 0)

    return (sum(multilist)%isbn_base) == 0



# greedy completions of ISBN by way of random plots at the end of the input.
# You can change to ISBN-13 by chancing isbn_base to 14, ISBN-10 to 11 etc. etc.

def isbn_auto_complete(isbn: str, isbn_base=11) -> str:

    #set size of completion
    random.seed(1264)
    k =  isbn_base - len(isbn.replace('-', '')) - 1

    if k < 0:
        raise ValueError("Too many numbers for completions of ISBN code")

    # plot random numbers until verification has been achieved (two 1-9 chars and ending char 1-10[ = X])
    while True:
        new_nums = random.choices([x + 1 for x in range(9)], k=(k-1))
        last_char = random.choice ([x + 1 for x in range(9)]+['X'])

        addendum = "".join(str(x) for x in new_nums) + str(last_char)
        isbn_new = isbn + addendum
        a = verify(isbn_new, isbn_base=isbn_base)
        if a:
            return isbn_new



