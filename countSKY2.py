# def count_chars(given_str,count_str=None):
#     count_dict={}
#     if count_str is None:
#         for char in given_str:
#             if char in count_dict:
#                 count_dict[char]+=1
#             else:
#                 count_dict[char]=1
#     else:
#         count_dict={my_char:given_str.count(my_char) for my_char in count_str}
#     return count_dict
#
#
# print(count_chars('Skyskysky12123hhffd','sky'))
# print(count_chars('srinivas'))

# print(count_chars('Skyskysky12123hhffd','sky'))
# print(count_chars('srinivas'))

#*****************************************************************************************#
def count_chars(given_str,count_str=''):
    mydict={}
    if not isinstance(given_str,str) or not isinstance(count_str,str):
        raise TypeError( 'Both parameters must be strings')
    elif count_str  == '':
        for char in given_str:
            if char in mydict:
                mydict[char]+=1
            else:
                mydict[char]=1
    else:
        mydict={char:0 for char in count_str}
        for char in given_str:
            if char in mydict:
                mydict[char]+=1
    return mydict

print(count_chars('skyskysky12123hhffd','sky')) #{'s': 3, 'k': 3, 'y': 3}
print(count_chars('srinivas')) #{'s': 2, 'r': 1, 'i': 2, 'n': 1, 'v': 1, 'a': 1}
print(count_chars('jhfgdfd','sky')) #{'s': 0, 'k': 0, 'y': 0}
print(count_chars('jhfgdfd')) #{'j': 1, 'h': 1, 'f': 2, 'g': 1, 'd': 2}
print(count_chars('','')) #{}
print(count_chars('12345','')) #{'1': 1, '2': 1, '3': 1, '4': 1, '5': 1}
#print(count_chars(12345,''))


#****************************************************************************************#

'''
mystr=['s','r','i','n','i','v','a','s']
print()
print(set(mystr)) #{'r', 'a', 'i', 'v', 's', 'n'}
print()
print(list(set(mystr))) #['r', 'a', 'i', 'v', 's', 'n']
print()
print(sorted(list(set(mystr)))) #['a', 'i', 'n', 'r', 's', 'v']
print()
print(sorted(list(set(mystr)),reverse=True)) #['v', 's', 'r', 'n', 'i', 'a']
print()
# list(set(mystr)).sort()
# print(mystr)
'''


# mystr='skySKY'
# mylist=[mystr.lower().count(x) for x in 'sky']
# print(mylist)
# print(f'S={mylist[0]}, K={mylist[1]}, Y={mylist[2]}')


# str='SKYSKYSKjhkjhjhkhfff'
# my_dict={}
# for char in str:
#     if char in my_dict:
#         my_dict[char]+=1
#     else:
#         my_dict[char]=1
# print(f'{my_dict}')

# str='SKYSKYSKjhkjhjhkhfff'
# mystrdict={char:0 for char in 'SKY'}
# #print(mystrdict)
# for char in str.upper():
#     if char in mystrdict:
#         mystrdict[char]+=1
# print(mystrdict)

















