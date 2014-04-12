import sys
import math
import utils
from utils import Tagger

def tag(words):
  trainingData = map((lambda str: str.rstrip("\n")), sys.stdin.readlines())
  tagger = Tagger(trainingData)
  return tagger.viterbi(words)
  
def main():
  trainingData = map((lambda str: str.rstrip("\n")), sys.stdin.readlines())
  tagger = Tagger(trainingData)

  wordsList = filter(lambda str: str != "", open("./data/entest").read().split("###/###"))
  testData = map(lambda str: filter(lambda str2: str2 != "", str.split("\n")), wordsList)


  # words = ["I", "was", "born" , "on" , "Oct." , "13", "."]
  # print tagger.viterbi(words)
  # sys.exit(0)

  # #checking
  # s, p = utils.get_pair_of_sentence_and_pos(testData[1])
  # for t in s:
  #   print t,
  # tagged = tagger.viterbi(s)

  # print zip(s, tagged)
  # sys.stdout.flush()
  # sys.exit(0)

  ok = 0
  ng = 0
  for td in testData:
    s, p = utils.get_pair_of_sentence_and_pos(td)
    tagged = tagger.viterbi(s)
    if len(tagged) != len(p):
      print "error"
    else:
      for i in range(0, len(p)):
        if tagged[i] == p[i]:
          ok += 1
        else:
          ng += 1

    sys.stdout.write(str(ok))
    sys.stdout.write(":")
    sys.stdout.write(str(ok+ng))
    sys.stdout.write(" ")
    print float(ok) / float(ok+ng)

  print ""
  print "---finished---"
  print float(ok) / float(ok+ng)
  
def experiment():
  trainingData = map((lambda str: str.rstrip("\n")), sys.stdin.readlines())
  


if __name__ == '__main__':
  main()
