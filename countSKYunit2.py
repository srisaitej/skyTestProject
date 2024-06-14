import unittest


def count_chars(given_str,count_str=''):
    mydict={}
    if given_str is None or count_str is None :
        '''if either or both the strings are None then it raises ValueError exception'''
        raise TypeError('The arguments cannot be None type and should be str type')
    elif not isinstance(given_str,str) or not isinstance(count_str,str):
        '''if either or both the strings are not of str type then it raises TypeError exception'''
        raise TypeError( 'Both parameters must be strings')
    elif count_str == '':
        '''If the count_str is empty then the count of every character in given_str is returned'''
        for char in given_str:
            if char in mydict:
                mydict[char]+=1
            else:
                mydict[char]=1


    else:
        '''This returns the count characters from the given_str that matches the characters in count_str'''
        mydict={char:0 for char in count_str}
        for char in given_str:
            if char in mydict:
                mydict[char]+=1
    return mydict





# print(count_chars('skyskysky12123hhffd','sky'))
# print(count_chars('srinivas'))
# print(count_chars('jhfgdfd','sky'))
# print(count_chars('jhfgdfd'))
# print(count_chars('',''))
# print(count_chars('12345',''))
#print(count_chars(12345,''))

class Testmycharcount(unittest.TestCase):


    def test_twoemptystrings(self):
        self.assertEqual(count_chars('',''),{},'two empty string passed as arguments')

    def test_alphanmeric(self):
        self.assertEqual(count_chars('skyskysky12123hhffd','sky'),{'s': 3, 'k': 3, 'y': 3},'Alphanumeric')

    def test_nosecondstring(self):
        self.assertEqual(count_chars('srinivas'),{'s': 2, 'r': 1, 'i': 2, 'n': 1, 'v': 1, 'a': 1},'no second string')

    def test_secondstringwithchars(self):
        self.assertEqual(count_chars('jhfgdfd','sky'),{'s': 0, 'k': 0, 'y': 0},'no secondstringchars')


    def test_firststringasnumeric(self):
        with self.assertRaises(TypeError):
            count_chars(12345, '')

    def test_secondstringasnumeric(self):
        with self.assertRaises(TypeError):
            count_chars('sky',12345)

    def test_bothstringsasnumeric(self):
        with self.assertRaises(TypeError):
            count_chars(12345,12345)

    def test_bothstringsasNone(self):
        with self.assertRaises(TypeError):
            count_chars(None,None)


if __name__=='__main__':
    unittest.main()

