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

  def test_get_num_of_word_same(self):
    input = ["###/###", "When/W", "such/J", "claims/N", "claims/N"]
    actual = utils.get_num_of_word_array(input)
    expected = {}
    expected["###"]=1
    expected["When"]=1
    expected["such"]=1
    expected["claims"]=2
    self.assertTrue(expected == actual)

  def test_get_num_of_pos(self):
    input = ["###/###", "When/W", "such/J", "claims/N"]
    actual = utils.get_num_of_pos_array(input)
    expected = {}
    expected["###"]=1
    expected["W"]=1
    expected["J"]=1
    expected["N"]=1
    self.assertTrue(expected == actual)

  def test_get_num_of_pos_same(self):
    input = ["###/###", "When/W", "such/J", "claims/N", "noun/N"]
    actual = utils.get_num_of_pos_array(input)
    expected = {}
    expected["###"]=1
    expected["W"]=1
    expected["J"]=1
    expected["N"]=2
    self.assertTrue(expected == actual)


if __name__ == '__main__':
  unittest.main()
