import unittest
import utils

class ReformCabochaTest(unittest.TestCase):
  def test_get_num_of_word(self):
    input = ["###/###", "When/W", "such/J", "claims/N"]
    actual = utils.get_num_of_word_array(input)
    expected = {}
    expected["###"]=1
    expected["When"]=1
    expected["such"]=1
    expected["claims"]=1
    self.assertTrue(expected == actual)




if __name__ == '__main__':
  unittest.main()
