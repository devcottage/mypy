import getopt, sys
import random
import string

help = sys.argv[0] + " <word-count>"

punctuation = ['_', '=', '+', '--']
all_words = tuple(open("wordlist.txt", 'r'))
phrase_words = list(map(lambda w: w.strip(), list(filter(lambda w: len(w) > 4 and len(w) < 10, all_words))))

args, vals = getopt.getopt(sys.argv[1:], "")
word_count = int(vals[-1] if len(vals) > 0 else 5)

# use random.choice() 
words = [random.choice(phrase_words) for _ in range(0,word_count - 1)]
words = list(map(lambda w : w.title().strip(), words))
words.append(str(random.randint(1000,9999)))
random.shuffle(words)

pass_phrase = words.pop()
for w in words:
    pass_phrase += random.choice(punctuation) + w

print(f"{word_count} words phrase, quoted \"{pass_phrase }\"")
