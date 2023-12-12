import getopt, sys
import random
import string

help = sys.argv[0] + " --caps --no-syms <password-length>"

# options
no_sym = False
caps = False

# always exclude quotes and JSON-ish bracket characters
excluded_chars = [ "'", '"', '\\', '`', '[', ']', '{', '}' ]
is_not_excluded = lambda ch : not ch in excluded_chars

allowed_chars = string.printable.strip()
allowed_chars = "".join(filter(is_not_excluded, allowed_chars))

long_opts = ["help", "all-caps", "no-syms"]
args, vals = getopt.getopt(sys.argv[1:], "", long_opts)
#print(args); print(vals)

try: 
  for arg in args:
    if arg[0] == "--help":
        throw
    elif arg[0] == "--all-caps":
        allowed_chars = allowed_chars.upper()
    elif arg[0] == "--no-syms":
        allowed_chars = "".join(filter(str.isalnum, allowed_chars))

  password_len = int(vals[-1] if len(vals) > 0 else 16)
except: 
   print(help)
   exit()

# use random.choice() to get password characters
passwd = [random.choice(allowed_chars) for _ in range(0,password_len)]

# extra randomization, via shuffle
for _ in range(random.randint(0,128)) : random.shuffle(passwd)
passwd = "".join(passwd)
if (caps):
  passwd = passwd.upper()

print(str(len(passwd)) + " character password, quoted : \"" + passwd + "\"")

