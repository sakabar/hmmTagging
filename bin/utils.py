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

  def get_pos_to_pos_log_p(self, pos1, pos2):
    n = self.n_pp[(pos1, pos2)]
    d = sum(map(lambda k: self.n_pp[k], filter(lambda pair: pair[1] == pos2 , self.n_pp.keys())))

    ans = float(n) / float(d)
    log_ans = math.log10(ans)

    return log_ans

  #fake
  def get_pos_to_word_log_p(self, pos, word):
    ans = -1

    return ans
    
  def viterbi(self, words):
    p_tbl = {(0,"###"):0.0}

    n = len(words)

    # for pos in self.n_p.keys():
    #   p_tbl[(1, pos)] = self.get_pos_to_pos_log_p("###", "N") + (words[j] from "N")
    

    #   for j in range(1,n+1):
    #     for k in range()
    
    # t[(1,"N")]=>y0*(y0 to "N")*(words[j] from "N")
    # t[(1,"P")]=>y0*(y0 to "P")*(words[j] from "P")
    
    
    return ["P", "V", "D", "N", "."]

    
