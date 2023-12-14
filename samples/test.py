import sys, glob, subprocess, os


import aggregate 

a = aggregate.aggregate([], "woof_", lambda x : str.isalnum(str(x)), lambda y : str.upper(str(y)))
print("".join(a))

b = aggregate.aggregate({}, "_woof", lambda x : str.isalnum(str(x)), lambda y : str.upper(str(y)))
print("".join(b.values()))

c = aggregate.aggregate({}, list("_woof"), lambda x : str.isalnum(str(x)), lambda y : str.upper(str(y)))
print("".join(c.values()))

d = aggregate.aggregate({}, dict(enumerate("_woof")), lambda x : str.isalnum(str(x)), lambda y : str.upper(str(y)))
print("".join(d.values()))

e = aggregate.aggregate({}, tuple("_woof"), lambda x : str.isalnum(str(x)), lambda y : str.upper(str(y)))
print("".join(e.values()))

f = aggregate.aggregate([], ['_','w','o','o','f'], lambda x : str.isalnum(str(x)), lambda y : str.upper(str(y)))
print("".join(f))

g = aggregate.aggregate({}, set(['_','w','o','O','f']), lambda x : str.isalnum(str(x)), lambda y : str.upper(str(y)))
print("".join(sorted(g.values(),reverse=True)))

import augment_sys_path as augment

wd = subprocess.run('pwd', stdout=subprocess.PIPE).stdout.decode().strip()
orig = tuple(sys.path)
print(orig)

augmented = augment.augment_sys_path(wd + "/**", recursive=True)
print(augmented)
print(f"augmentation: {set(augmented) - set(orig)}")
