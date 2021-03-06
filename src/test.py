#coding: utf-8
import unittest
import math
import utils
from utils import Tagger

class HmmTaggingTest(unittest.TestCase):
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

  def test_get_num_of_word_and_pos(self):
    input = ["###/###", "When/W", "such/J", "claims/N", "noun/N", "claims/N"]
    actual = utils.get_num_of_word_and_pos_array(input)
    expected = {}
    expected[("###","###")]=1
    expected[("When", "W")]=1
    expected[("such", "J")]=1
    expected[("claims", "N")]=2
    expected[("noun", "N")]=1
    self.assertTrue(expected == actual)

  def test_p_p(self):
    lst = ["###/###", "I/P", "have/V", "a/D", "book/N", "./."]
    
    actual = utils.get_pos_to_pos(lst)

    expected = {}
    expected[("###","P")]=1
    expected[("P", "V")]=1
    expected[("V", "D")]=1
    expected[("D", "N")]=1
    expected[("N", ".")]=1
    self.assertEquals(expected, actual)

  def test_viterbi(self):
    train = ["###/###", "I/P", "have/V", "a/D", "book/N", "./."]
    words = ["I", "have", "a", "book", "."]
    tagger = Tagger(train)
    
    actual = tagger.viterbi(words)
    expected = ["P", "V", "D", "N", "."]
    self.assertEquals(expected, actual)

  def test_get_pos_to_pos_log_p(self):
    train = ["###/###", "I/P", "have/V", "a/D", "book/N", "./."]
    tagger = Tagger(train)

    actual = tagger.get_pos_to_pos_log_p("###", "P")
    expected = math.log10((1.0+1.0) / (1.0+1.0*6))
    self.assertEquals(expected, actual)

  def test_get_pos_to_word_log_p(self):
    train = ["###/###", "I/P", "have/V", "a/D", "book/N", "./."]
    tagger = Tagger(train)

    actual = tagger.get_pos_to_word_log_p("V", "have")
    expected = math.log10((1.0+1.0) / (1.0 + 1.0*(6+1)))
    self.assertEquals(expected, actual)

  def test_vocab_num(self):
    train = ["###/###", "I/P", "have/V", "a/D", "book/N", "./.", "I/P"]
    tagger = Tagger(train)

    actual = tagger.vocab_num
    expected = 6 + 1 #未知語UNKNOWN含む
    self.assertEquals(expected, actual)

  def test_tag_num(self):
    train = ["###/###", "I/P", "have/V", "a/D", "book/N", "./.", "I/P"]
    tagger = Tagger(train)

    actual = tagger.tag_num
    expected = 6
    self.assertEquals(expected, actual)

  def test_get_sentence_and_pos(self):
    actual = utils.get_pair_of_sentence_and_pos(["I/P", "have/V", "a/D", "book/N", "./."])
    expected = (["I", "have", "a", "book", "."], ["P", "V", "D", "N", "."])
    self.assertEquals(expected, actual)
    
if __name__ == '__main__':
  unittest.main()
