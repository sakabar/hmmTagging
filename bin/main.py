import sys
import math
import utils
from utils import Tagger

def main():
  words = ["I", "have", "a", "book"]
  wpList = map((lambda str: str.rstrip("\n")), sys.stdin.readlines())
  tagger = Tagger(wpList)
  print tagger.viterbi(words)


if __name__ == '__main__':
  main()
