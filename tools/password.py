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

# start out with all printable characters
allowed_chars = string.printable.strip()
allowed_chars = "".join(filter(is_not_excluded, allowed_chars))

# handle command-line options
long_opts = ["help", "all-caps", "no-syms"]
args, vals = getopt.getopt(sys.argv[1:], "", long_opts)
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
passwd = "".join(passwd)
if (caps):
  passwd = passwd.upper()

print(str(len(passwd)) + " character password:\n", file=sys.stderr)
print(passwd); print("", file=sys.stderr)
