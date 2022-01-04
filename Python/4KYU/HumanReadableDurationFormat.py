def format_duration(seconds):
    if seconds == 0:
        return 'now'
    string = ''
    
    if (seconds // (60 * 60 * 24 * 365)) > 1:
        string += f'{seconds // (60 * 60 * 24 * 365)} years, '
    elif (seconds // (60 * 60 * 24 * 365)) == 1:
        string += f'{seconds // (60 * 60 * 24 * 365)} year, '
    seconds -= (seconds // (60 * 60 * 24 * 365)) * 60 * 60 * 24 * 365
    
    if (seconds // (60 * 60 * 24)) > 1:
        string += f'{seconds // (60 * 60 * 24)} days, '
    elif (seconds // (60 * 60 * 24)) == 1:
        string += f'{seconds // (60 * 60 * 24)} day, '
    seconds -= (seconds // (60 * 60 * 24)) * 60 * 60 * 24
    
    if (seconds // (60 * 60)) > 1:
        string += f'{seconds // (60 * 60)} hours, '
    elif (seconds // (60 * 60)) == 1:
        string += f'{seconds // (60 * 60)} hour, '
    seconds -= (seconds // (60 * 60)) * 60 * 60
    
    if seconds // 60 > 1:
        string += f'{seconds // 60} minutes, '
    elif seconds // 60 == 1:
        string += f'{seconds // 60} minute, '
    seconds -= (seconds // 60) * 60
    
    if seconds > 1:
        string += f'{seconds} seconds, '
    elif seconds == 1:
        string += f'{seconds} second, '

    return string[:-2][::-1].replace(",","dna ",1)[::-1]
    