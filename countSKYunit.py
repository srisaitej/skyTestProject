from collections import Counter

def count_chars(givenstr,checkstr):
    count_letters=Counter(givenstr)
    print(count_letters)
    #print(type(count_letters))
    result={char:count_letters.get(char,0) for char in checkstr}
    print(result)
    print()
    return result

count_chars('skyfhjdsky12345','sky')
count_chars('fhjd12345','sky')
count_chars('sky','')





