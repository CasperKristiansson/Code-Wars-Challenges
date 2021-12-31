# https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python

def domain_name(url):   
    if (url.find('//www.') != -1):
        url = url[url.find('//') + 6:]
    elif url.find('//') != -1:
        url = url[url.find('//') + 2:]
    elif url.find('www.') != -1:
        url = url[url.find('www.') + 4:]
    return url[:url.find('.')]
