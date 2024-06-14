from collections import Counter
import unittest


def count_letters(string,letters_to_count):
  """
  Count the occurences of the elements in the given string
  :param input_string:
  :param letters_to_count:
  :return:
  Returns dictionary like object where key is the element and val is the corresponding count
  Raises:
  Raises exceptions error(TyepError,ValueError)
  """

  if string is None or letters_to_count is None:
      raise ValueError('both must be provided')

  if not isinstance(string,str) or not isinstance(letters_to_count,str):
      raise TypeError('both must be strings')

  if not string or not letters_to_count:
      return {}

  rescount = {}

  for letter in letters_to_count:
      rescount[letter]= string.count(letter)
#  print(rescount)
  return rescount





class TestcountLetters(unittest.TestCase):

    def test_valid_case(self):
        # Test1 - check valid sring and letters
        self.assertEqual(count_letters("Hello SKy", "SKY"), {
            'S': 1,
            'K': 1,
            'Y': 0
        })

    def test_empty_string(self):
        # Test2 - chcek empty string
        self.assertEqual(count_letters('', 'SKY'), {})

    def test_empty_letters(self):
        # Test3 - check empty letters
        self.assertEqual(count_letters('SKY', ''), {})


    def test_input_none(self):
        # Test4 - check None input string
        with self.assertRaises(ValueError):
            count_letters(None, 'SKY')

    def test_input_letters_none(self):
        # Test5 - check None  input letters
        with self.assertRaises(ValueError):
            count_letters('SKY', None)

    def test_non_string_input_string(self):
        # Test6 - check non input string
        with self.assertRaises(TypeError):
            count_letters(111, 'SKY')

    def test_non_string_input_letters(self):
        # Test7 - Check non input letters
        with self.assertRaises(TypeError):
            count_letters('SKY', 111)


if __name__ == "__main__":
    unittest.main()
