import sys

def calc_score(word_fragment):
  fragment = list(word_fragment)
  score = 1
  score_one = ['a', 'b', 'd', 'e', 'g', 'i', 'n', 'o', 'r', 's', 't', 'u']
  score_two = ['c', 'f', 'h', 'l', 'm', 'p', 'v', 'w', 'y']
  score_three = ['j', 'k', 'q', 'x', 'z']
  score += sum([fragment.count(w) for w in score_one])
  score += sum([fragment.count(w)*2 for w in score_two])
  score += sum([fragment.count(w)*3 for w in score_three])
  return score**2
  
calc_score(sys.argv[1])
