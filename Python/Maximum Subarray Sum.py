# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/train/python

def max_sequence(arr):
    total = 0
    for i in range(len(arr)):
        for j in range(len(arr), -1, -1):
            if(sum(arr[i:j + 1]) > total):
                total = sum(arr[i:j + 1])
    
    return total

# Other solutions with O(n) time complexity
def maxSequence(arr):
    maxl = 0
    maxg = 0
    for n in arr:
        maxl = max(0, maxl + n)
        maxg = max(maxg, maxl)
        print(maxl, maxg)
    return maxg