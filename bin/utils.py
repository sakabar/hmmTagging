import math

def get_num_of_word_array(lst):
  ans = {}

  for item in lst:
    (w, p) = item.split("/")
    if w in ans:
      ans[w] += 1
    else:
      ans[w] = 1

  return ans

def get_num_of_pos_array(lst):
  ans = {}

  for item in lst:
    (w, p) = item.split("/")
    if p in ans:
      ans[p] += 1
    else:
      ans[p] = 1

  return ans

def get_num_of_word_and_pos_array(lst):
  ans = {}

  for item in lst:
    (w, p) = item.split("/")
    if (w,p) in ans:
      ans[(w,p)] += 1
    else:
      ans[(w,p)] = 1

  return ans

def get_pos_to_pos(wpList):
  lst = map((lambda str: str.split("/")[1]), wpList)
  ans = {}

  for i in range(1,len(lst)):
    if (lst[i-1], lst[i]) in ans:
      ans[(lst[i-1], lst[i])] += 1
    else:
      ans[(lst[i-1], lst[i])] = 1

  return ans
  
class Tagger:
  def __init__(self, wpList):
    self.wpList = wpList
    self.n_w = get_num_of_word_array(wpList)
    self.n_p = get_num_of_pos_array(wpList)
    self.n_wp = get_num_of_word_and_pos_array(wpList)
    self.n_pp = get_pos_to_pos(wpList)
    self.vocab_num = len(self.n_w.keys())
    self.tag_num = len(self.n_p.keys())
    self.eps = 1.0

    
  def get_pos_to_pos_log_p(self, pos1, pos2):
    if (pos1, pos2) in self.n_pp:
      n = self.n_pp[(pos1, pos2)] + self.eps
    else:
      n = self.eps

    d = sum(map(lambda k: self.n_pp[k], filter(lambda pair: pair[1] == pos2 , self.n_pp.keys()))) + self.eps * self.vocab_num

    ans = float(n) / float(d)
    log_ans = math.log10(ans)

    return log_ans

  def get_pos_to_word_log_p(self, pos, word):
    if (word, pos) in self.n_wp:
      n = self.n_wp[(word, pos)] + self.eps
    else:
      n = self.eps

    d = self.n_p[pos] + self.eps * self.tag_num
    
    ans = float(n) / float(d)
    log_ans = math.log10(ans)

    return log_ans

  #fake
  def viterbi(self, words):
    p_tbl = {(0,"###"):0.0}

    n = len(words)

    for j in range(1,n):
      for pos in self.n_p.keys():
        p_tbl[(1, pos)] = self.get_pos_to_pos_log_p("###", pos) + self.get_pos_to_word_log_p(pos, words[j])
    
      # for j in range(1,n+1):
      #   for k in range()

    
    # t[(1,"N")]=>y0*(y0 to "N")*(words[j] from "N")
    # t[(1,"P")]=>y0*(y0 to "P")*(words[j] from "P")
    
    
    return ["P", "V", "D", "N", "."]

    
