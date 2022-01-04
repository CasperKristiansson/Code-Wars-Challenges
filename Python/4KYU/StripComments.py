def solution(string, markers):
    string = string.split('\n')
    result = ''
    
    for line in string:
        for character in line:
            if character not in markers:
                result += character
            else:
                result = result[:-1]
                break
        result += '\n'
                
    return result[:-1]

#Alternative solution
def solution(string, markers):
    lines = string.split('\n')
    
    for index, line in enumerate(lines):
        for marker in markers:
            if line.find(marker) != -1:
                line = line[:line.find(marker)]
                
        lines[index] = line.rstrip(' ')
        
    return '\n'.join(lines)
