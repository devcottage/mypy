import getopt, sys
import random
import string

help = sys.argv[0] + " --caps --no-syms <password-length>"

# exclude quotes and JSON-ish bracket characters, 
#   to make scripting and cut-and-paste easier
excluded_chars = [ "'", '"', '\\', '`', '[', ']', '{', '}' ]
is_not_excluded = lambda ch : not ch in excluded_chars

# start out with all printable characters, and prune excuded ones
allowed_chars = string.printable.strip()
allowed_chars = "".join(filter(is_not_excluded, allowed_chars))

# handle command-line options
long_opts = ["help", "all-caps", "no-syms"]
args, vals = getopt.getopt(sys.argv[1:], "", long_opts)
try: 
  for arg in args:
    if arg[0] == "--help":
        raise RuntimeWarning()
    elif arg[0] == "--all-caps":
        allowed_chars = allowed_chars.upper()
    elif arg[0] == "--no-syms":
        allowed_chars = "".join(filter(str.isalnum, allowed_chars))

  password_len = int(vals[-1] if len(vals) > 0 else 16)
except: 
   print(help)
   exit()

# use random.choice() of unique set of allowed chars to get password 
choices = list(set(allowed_chars))
passwd = [random.choice(choices) for _ in range(0,password_len)]
passwd = "".join(passwd)

print(str(len(passwd)) + " character password:\n", file=sys.stderr)
print(passwd); print("", file=sys.stderr)
