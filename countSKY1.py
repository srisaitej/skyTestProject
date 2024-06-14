import unittest

def countSKY(mystr):

  if not isinstance(mystr,str):
      raise TypeError('The parameter should be of str type')
  else:
    # mystr=mystr.upper()
    countS = mystr.count('S')
    counts = mystr.count('s')
    countK = mystr.count('K')
    countk = mystr.count('k')
    countY = mystr.count('Y')
    county = mystr.count('y')
    return countS+counts, countK+countk, countY+county


class TestCharCount(unittest.TestCase):
  def test_charsonly(self):
    self.assertEqual(countSKY('skySKYskyfjfljwewe'),(3,3,3),'Verify the count of letters S K Y in chars only string')


  def test_alphanumeric(self):
    self.assertEqual(countSKY('1234SKYuioiert8989'),(1,1,1),'Verify the count of letters s k y in alphanumeric only string')

  def test_emptystring(self):
    self.assertEqual(countSKY(''),(0,0,0),'Verify the count of letters s k y in alphanumeric only string')

  def test_none(self):
    with self.assertRaises(TypeError):
      countSKY(None)

  def test_numbers(self):
    with self.assertRaises(TypeError):
      countSKY(12345)


if __name__=='__main__':
  unittest.main()





# def count_chars(given_str, count_str=''):
#     mydict = {}
#     if count_str == '':
#       '''If the count_str is empty then the count of every character in given_str is returned'''
#       for char in given_str:
#         if char in mydict:
#           mydict[char] += 1
#         else:
#           mydict[char] = 1
#     else:
#       '''This returns the count characters from the given_str that matches the characters in count_str'''
#       mydict = {char: 0 for char in count_str}
#       for char in given_str:
#         if char in mydict:
#           mydict[char] += 1
#     return mydict
#
# print(count_chars('skyskysky12123hhffd','sky'))
# print(count_chars('srinivas'))
# print(count_chars('jhfgdfd','sky'))
# print(count_chars('jhfgdfd'))
# print(count_chars('',''))
# print(count_chars('srinivas',''))
# try:
#   print(count_chars(None,''))
# except (TypeError) as e:
#   print(e)
