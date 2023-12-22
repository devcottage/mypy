import getopt, sys, os
import random
import string

help = sys.argv[0] + " --with-nums <n> --seperator <word-seperator> --maxword <max-word-length> <word-count> "

punctuation = ['_', '=', '+', '--', '.', ',']

tool_dir = os.path.dirname(os.path.abspath(__file__))
all_words = tuple(open(os.path.join(tool_dir, "wordlist.txt"), 'r'))
max_word_len = 16
num_count = 0

# handle command-line options
opts,args = getopt.getopt(sys.argv[1:], "hs:vm:vw:v", ["help", "seperator=", "maxword=", "with-nums"])
try: 
  for o,v in opts:
    if o in ("-h", "--help"):
        throw
    elif o in ("-s", "--seperator"):
        punctuation = [v]
    elif o in ("-m", "--maxwor"):
        max_word_len = int(v)
    elif o in ("-w", "--with-nums"):
        num_count = int(v)

  word_count = int(args[-1] if len(args) > 0 else 5)
except Exception as ex: 
   print(help)
   exit()

# gather raw material
phrase_words = list(map(lambda w: w.strip(), list(filter(lambda w: len(w) <= max_word_len, all_words))))
print(f"dictionary size={len(phrase_words)}", file=sys.stderr)

# use random.choice() for words in phrase, and add in a number sequence, usually required
words = [random.choice(phrase_words) for _ in range(word_count)]
words = list(map(lambda w : w.title().strip(), words))
for c in range(num_count):
    words.append(str(random.randint(1000,99999)))

random.shuffle(words)

# add punctuation (symbols) as word seperators to make it easier to type
pass_phrase = (words if len(words) > 0 else [""]).pop()
for w in words:
    pass_phrase += random.choice(punctuation) + w

print(f"{word_count} word(s) + {num_count} number / {len(pass_phrase)} character phrase, with punctuation:\n", file=sys.stderr)
print(f"{pass_phrase}"); print("", file=sys.stderr)
