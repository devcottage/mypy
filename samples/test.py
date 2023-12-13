import sys, glob, subprocess, os


import aggregate 

a = aggregate.aggregate([], "woof_", lambda x : str.isalnum(str(x)), lambda y : str.upper(str(y)))
print("".join(a))

b = aggregate.aggregate({}, "_woof", lambda x : str.isalnum(str(x)), lambda y : str.upper(str(y)))
print("".join(b.values()))

try:
    c = aggregate.aggregate(tuple({}), "woof", lambda x : str.isalnum(str(x)), lambda y : str.upper(str(y)))
except TypeError: 
    pass


import augment_sys_path as augment

wd = subprocess.run('pwd', stdout=subprocess.PIPE).stdout.decode().strip()
orig = tuple(sys.path)
print(orig)

augmented = augment.augment_sys_path(wd + "/**", recursive=True)
print(augmented)
print(f"augmentation: {set(augmented) - set(orig)}")
