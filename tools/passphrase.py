import getopt, sys, os
import random
import string

help = sys.argv[0] + " <word-count>"

punctuation = ['_', '=', '+', '--']

tool_dir = os.path.dirname(os.path.abspath(__file__))
all_words = tuple(open(os.path.join(tool_dir, "wordlist.txt"), 'r'))
phrase_words = list(map(lambda w: w.strip(), list(filter(lambda w: len(w) > 4 and len(w) < 13, all_words))))

args, vals = getopt.getopt(sys.argv[1:], "")
word_count = int(vals[-1] if len(vals) > 0 else 5)

# use random.choice() for words in phrase, and add in a number character, which is usually required
words = [random.choice(phrase_words) for _ in range(0,word_count - 1)]
words = list(map(lambda w : w.title().strip(), words))
words.append(str(random.randint(1000,9999)))
random.shuffle(words)

# add punctuation (symbols) as word seperators
pass_phrase = words.pop()
for w in words:
    pass_phrase += random.choice(punctuation) + w

print(f"{word_count} word/{len(pass_phrase)} character phrase:\n", file=sys.stderr)
print(f"{pass_phrase}"); print("", file=sys.stderr)
