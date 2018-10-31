import random, re

def verify(isbn: str, isbn_base=11, sanity=True):

    isbn_s = isbn.lower().replace('-', '') #strip comas if needed

    #Sanity checks

    char_check = re.findall(r'[a-wyz]', isbn_s)
    if char_check != []:
        raise ValueError("Invalid characters in input [ISBN can only contain nubmers and an optional x as the last character]")

    if len(isbn_s) != (isbn_base-1) and sanity == True:
        raise ValueError("Too many or too few characters in input")

    if 'x' in isbn_s and isbn_s[-1] !='x' and sanity == True:
        raise ValueError("X can only appear at the end of the ISBN code. \nEither the complete ISBN provided is wrong"
                         "or you have provided a beginning of an ISBN for auto-completion and it contains an \'x\' ")
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
    print((sum(multilist)%isbn_base) == 0)

    return (sum(multilist)%isbn_base) == 0



def isbn_auto_complete(isbn: str, isbn_base=11):
    random.seed(1264)
    k =  isbn_base - len(isbn.replace('-', '')) - 1

    if k < 0:
        raise ValueError("Too many numbers for completions of ISBN code")

    while True:
        new_nums = random.choices([x + 1 for x in range(9)], k=(k-1))
        last_char = random.choice ([x + 1 for x in range(9)]+['X'])

        addendum = "".join(str(x) for x in new_nums) + str(last_char)
        isbn_new = isbn + addendum
        a = verify(isbn_new, isbn_base=isbn_base, sanity=True)
        if a:
            break

    # for debugging
    print(isbn_new)
    return isbn_new

# code = '3-598-21508-8'
# # # verify(code)
# # isbn_auto_complete(code, isbn_base=14)
#
# verify('35982F1507', isbn_base=11, sanity=True)
#

