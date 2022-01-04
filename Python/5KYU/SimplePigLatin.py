def pig_it(text):
    text = text.split()
    for i in range(len(text)):
        if text[i] not in ('!', '?'):
            text[i] = text[i][1:] + text[i][0] + 'ay'

    return ' '.join(text)