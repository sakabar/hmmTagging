#coding: utf-8
import math
import sys

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
  lst = [s.split("/")[1] for s in wpList]
  ans = {}

  for i in range(1,len(lst)):
    if (lst[i-1], lst[i]) in ans:
      ans[(lst[i-1], lst[i])] += 1
    else:
      ans[(lst[i-1], lst[i])] = 1

  return ans

def maximum(prob_pos_pair):
  ans_prob = - 1000.0 #magic num
  ans_pos = "###"

  for (prob, pos) in prob_pos_pair:
    if prob >= ans_prob:
      ans_prob = prob
      ans_pos = pos

  return (ans_prob, ans_pos)

def get_pair_of_sentence_and_pos(wpList):
  ans_s = []
  ans_p = []

  for wp in wpList:
    tmp_s , tmp_p = wp.split("/")
    ans_s.append(tmp_s)
    ans_p.append(tmp_p)

  return (ans_s, ans_p)

def zip(lst1, lst2):
  n = min(len(lst1), len(lst2))
  ans = []
  
  for i in range(0, n):
    ans += (lst1[i], lst2[i])

  return ans
  
class Tagger:
  def __init__(self, wpList):
    self.wpList = wpList
    self.n_w = get_num_of_word_array(wpList)
    self.n_w["UNKNOWN"] = 0 #未知語
    
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

    l = map(lambda k: self.n_pp[k], filter(lambda pair: pair[1] == pos2 , self.n_pp.keys()))
    d = sum(l) + self.eps * self.tag_num

    ans = float(n) / float(d)
    log_ans = math.log10(ans)

    return log_ans

  def get_pos_to_word_log_p(self, pos, word):
    if (word, pos) in self.n_wp:
      n = self.n_wp[(word, pos)] + self.eps
    else:
      n = self.eps

    d = self.n_p[pos] + self.eps * self.vocab_num
    
    ans = float(n) / float(d)
    log_ans = math.log10(ans)

    return log_ans

  def viterbi(self, input_words):
    words = ["###"] + input_words
    logp_tbl = {(0,"###") : (0.0, "###")}

    n = len(words)

    #前向き
    for pos in self.n_p.keys():
      logp_tbl[(1, pos)] = (self.get_pos_to_pos_log_p("###", pos) + self.get_pos_to_word_log_p(pos, words[1]), "###")

    for j in range(2,n):
      for pos in self.n_p.keys():
        logp_tbl[(j, pos)] = maximum(map(lambda prev_pos: (logp_tbl[(j-1, prev_pos)][0] + self.get_pos_to_pos_log_p(prev_pos, pos) + self.get_pos_to_word_log_p(pos, words[j]), prev_pos), self.n_p.keys()))

    #バックトラック
    tmp = -1000000.0 #magic
    last_pos = "###" #magic
    for pos in self.n_p.keys():
      if logp_tbl[(n-1, pos)][0] >= tmp:
        last_pos = pos
        tmp = logp_tbl[(n-1, pos)][0]

    ans = [last_pos]
    tmp_pos = last_pos

    for j in range(n-1, 1, -1):
      tmp_pos = logp_tbl[(j, tmp_pos)][1]
      ans.append(tmp_pos)
    ans.reverse()

    return ans

    
