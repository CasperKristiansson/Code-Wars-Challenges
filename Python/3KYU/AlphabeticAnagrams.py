# Not Completed Due to time - https://www.codewars.com/kata/53e57dada0cb0400ba000688/train/python

from itertools import permutations
import time

# def listPosition(word):

#     words = [''.join(j) for j in permutations(word, len(word))]
#     words = sorted(set(words))
#     return words.index(word)

# start = time.time()
# listPosition('eniqjwenqweqwa')
# end = time.time()
# print(end - start)


def listPosition(word):
    if len(word) == 1:
        return 1
    
    words = sorted(word)
    perm = permutation(list(words), list(word))
    
    return 0

def permutation_old(lst, word):
    if len(lst) == 1:
        return [lst]
    
    l = []
    

    for i in range(len(lst)):
        m = lst[i]

        remainderLst = lst[:i] + lst[i+1:]
        for p in permutation_old(remainderLst, word):
            l.append([m] + p)
            if [m] + p == word:
                return l
            print(l)
    return l  
    
listPosition('ABAB')
