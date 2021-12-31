# https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/train/python

def solution(args):
    print(args)
    i = j = 0
    result = []
    section = []
    
    while i < len(args):
        section.append(str(args[j]))
        while j + 1 < len(args) and args[j] + 1 == args[j + 1]:
            section.append(str(args[j + 1]))
            j += 1
            
        if(len(section) > 2):
            result.append(section[0] + '-' + section[-1])
        else:
            result.extend(section)
            
        i += len(section)
        j = i
        section = []
    
    return ','.join(result)
