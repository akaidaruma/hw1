import pandas as pd
import itertools
from bisect import bisect_left

dictionary = pd.read_csv('master_dictionary_nonU.csv')
wordlist = list(dictionary['Changed'])
ans = list(dictionary['Word'])

print("word pannels:")
target = list(input())
target.sort()
target = ''.join(target)

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

def make_kouho(pannel, num):
    kouho = []
    for x in itertools.combinations(pannel, num):
        kouho.append(''.join(x))
    return kouho

def word_exists(wordlist, word_fragment, answerlist, scorelist):
    position = bisect_left(wordlist, word_fragment)
    if position != len(wordlist): #エラー避けのif文(よくわかってない)
        if wordlist[position] == word_fragment:
            if ans[position] not in answerlist:
                scorelist.append((calc_score(word_fragment)))
                answerlist.append(ans[position])
            return answerlist, scorelist           

def make_word(pannel):
    for i in range(16, 1, -1):
        kouholist = make_kouho(pannel, i)
        for kouho in kouholist:
            word_exists(wordlist, kouho, answerlist, scorelist)
    return answerlist, scorelist

answerlist = []
scorelist = []
answerlist, scorelist = make_word(target)
print(answerlist[scorelist.index(max(scorelist))])