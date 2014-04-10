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
