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

  for wp in lst:
    if wp in ans:
      ans[wp] += 1
    else:
      ans[wp] = 1

  return ans

class Tagger:
  def __init__(self, wpList):
    self.wpList = wpList
    self.n_w = get_num_of_word_array(wpList)
    self.n_p = get_num_of_pos_array(wpList)
    self.n_wp = get_num_of_word_and_pos_array(wpList)

  def viterbi(words):
    t = {(0,"###"):0.0}
    n = len(words)

#   for j in range(1,n+1):
#     for k in range()

# t[(1,"N")]=>y0*(y0 to "N")*(words[j] from "N")
# t[(1,"P")]=>y0*(y0 to "P")*(words[j] from "P")

    return ["P", "V", "D", "N"]
