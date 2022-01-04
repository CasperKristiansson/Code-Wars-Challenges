def make_readable(seconds):
    string = (
        f'0{seconds // (60 ** 2)}:'
        if (seconds // (60 ** 2)) < 10
        else f'{seconds // (60 ** 2)}:'
    )
    seconds -= seconds // 60**2 * 60 * 60

    string += (
        f'0{seconds // (60)}:'
        if (seconds // (60)) < 10
        else f'{seconds // (60)}:'
    )
    seconds -= seconds // (60) * 60

    string += f'0{seconds}' if seconds < 10 else f'{seconds}'
    return string