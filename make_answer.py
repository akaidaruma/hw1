import pandas as pd
from bisect import bisect_left

dictionary = pd.read_csv('master_dictionary.csv')
wordlist = list(dictionary['Changed'])
ans = list(dictionary['Word'])

print("word pannels:")
target = list(input())
target.sort()
target = ''.join(target)

def word_exists(wordlist, word_fragment):
    if wordlist[bisect_left(wordlist, word_fragment)].startswith(word_fragment):
        print(ans[bisect_left(wordlist, word_fragment)])
    else:
        print("No answer")

word_exists(wordlist, target)
