import getopt, sys, os
import random
import string

help = sys.argv[0] + " --seperator <word-seperator>  <word-count>"

punctuation = ['_', '=', '+', '--', '.', ',']

tool_dir = os.path.dirname(os.path.abspath(__file__))
all_words = tuple(open(os.path.join(tool_dir, "wordlist.txt"), 'r'))
phrase_words = list(map(lambda w: w.strip(), list(filter(lambda w: len(w) > 4 and len(w) < 13, all_words))))
print(f"dictionary size={len(phrase_words)}", file=sys.stderr)

# handle command-line options
opts,args = getopt.getopt(sys.argv[1:], "hs:v", ["help", "seperator="])
try: 
  for o,v in opts:
    if o in ("-h", "--help"):
        throw
    elif o in ("-s", "--seperator"):
        punctuation = [v]

  word_count = int(args[-1] if len(args) > 0 else 5)
except Exception as ex: 
   print(help)
   exit()

# use random.choice() for words in phrase, and add in a number sequence, usually required
words = [random.choice(phrase_words) for _ in range(word_count)]
words = list(map(lambda w : w.title().strip(), words))
words.append(str(random.randint(1000,9999)))
random.shuffle(words)

# add punctuation (symbols) as word seperators to make it easier to type
pass_phrase = words.pop()
for w in words:
    pass_phrase += random.choice(punctuation) + w

print(f"{word_count} word(s) + 1 number / {len(pass_phrase)} character phrase, with punctuation:\n", file=sys.stderr)
print(f"{pass_phrase}"); print("", file=sys.stderr)
