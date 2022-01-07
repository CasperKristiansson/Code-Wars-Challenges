def permutations(string):
    permutations = permutation(list(string))
    for i in range(len(permutations)):
        permutations[i] = ''.join(permutations[i])
        
    return sorted(set(permutations))
    
def permutation(permutation_list):
    if len(permutation_list) == 1:
        return [permutation_list]

    new_list = []

    for i in range(len(permutation_list)):
        for p in permutation(permutation_list[:i] + permutation_list[i+1:]):
            new_list.append([permutation_list[i]] + p)
    return new_list