# def countSKY(mystr,countstr):


    # mystr=mystr.upper()
    # countS = mystr.count('S')
    # counts = mystr.count('s')
    # countK = mystr.count('K')
    # countk = mystr.count('k')
    # countY = mystr.count('Y')
    # county = mystr.count('y')
    # return countS+counts, countK+countk, countY+county
    #
    # dict={}







# s,k,y=countSKY('sky is blue','abcd')
# print(f's={s}, k={k}, y={y}')

def countSKY(str1,str2):
    mydict = {char: 0 for char in str2}
    for char in str1:
        if char in mydict:
            mydict[char] += 1
    return mydict

mycount = countSKY('sky is blue','sky')

for key,value in mycount.items():
    print(f'{key} : {value}')