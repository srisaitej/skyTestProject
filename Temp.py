# def myprint(a):
#     print(int(a))
#
#
# myprint('abc')

mystr='sri'
if mystr !='':
    print(mystr)

# def count_chars(given_str,count_str):
#     mydict={}
#     if count_str == '':
#         '''If the count_str is empty then the count of every character in given_str is returned'''
#         for char in given_str:
#             if char in mydict:
#                 mydict[char] += 1
#             else:
#                 mydict[char] = 1
#     else:
#         '''This returns the count characters from the given_str that matches the characters in count_str'''
#         mydict = {char: 0 for char in count_str}
#         for char in given_str:
#             if char in mydict:
#                 mydict[char] += 1
#         return mydict
#
#
# count_chars(1234,12345)




# from collections import Counter
#
#
# def count_letters(string, letters):
#     letter_counts = Counter(string)
#     result = {letter: letter_counts.get(letter, 0) for letter in letters}
#
#     return result
#
#
# string = 'SKY'
# letters_to_count = 'SKY'
# result = count_letters(string, letters_to_count)
# print(result)
#
