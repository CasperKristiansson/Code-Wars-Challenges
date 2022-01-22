def mix(s1, s2):
    s1_dic = {}
    s2_dic = {}
    for letter in s1:
        if not letter.isalpha() or letter.isupper():
            continue

        if letter in s1_dic:
            s1_dic[letter] += 1
        else:
            s1_dic[letter] = 1

    for letter in s2:
        if not letter.isalpha() or letter.isupper():
            continue

        if letter in s2_dic:
            s2_dic[letter] += 1
        else:
            s2_dic[letter] = 1

    for key, value in dict(s1_dic).items():
        if value <= 1:
            del s1_dic[key]
        elif key in s2_dic and s2_dic[key] > value:
            del s1_dic[key]

    for key, value in dict(s2_dic).items():
        if value <= 1:
            del s2_dic[key]
        elif key in s1_dic and s1_dic[key] > value:
            del s2_dic[key]
    
    
    string = ''
    string_equal = ''
    dictionary = dict((s1_dic | s2_dic))


    for key, value in dict(sorted(dictionary.items(), key=lambda x: (-x[1], x[0]))).items():
        if key in s1_dic and key in s2_dic:
            string_equal += "=:" + key * value + "/"
        elif key in s1_dic:
            string += "1:" + key * value + "/"
        elif key in s2_dic:
            string += "2:" + key * value + "/"

    return string + string_equal[:-1]


print(mix("Are they here", "yes, they are here") == "2:eeeee/2:yy/=:hh/=:rr")
print(mix("Sadus:cpms>orqn3zecwGvnznSgacs","MynwdKizfd$lvse+gnbaGydxyXzayp") == '2:yyyy/1:ccc/1:nnn/1:sss/2:ddd/=:aa/=:zz')
