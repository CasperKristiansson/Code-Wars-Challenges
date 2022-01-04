def array_diff(a, b):
    i = 0
    if len(b) == 0:
        return a
    while i < len(a):
        if a[i] in b:
            del a[i]
            i -= 1
        else:
            i += 1
    
    return a
