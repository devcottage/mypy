import aggregate 

a = aggregate.aggregate([], "woof", lambda x : str.isalnum(str(x)), lambda y : str.upper(str(y)))
print("".join(a))

b = aggregate.aggregate({}, "woof", lambda x : str.isalnum(str(x)), lambda y : str.upper(str(y)))
print("".join(b.values()))

try:
    c = aggregate.aggregate(tuple({}), "woof", lambda x : str.isalnum(str(x)), lambda y : str.upper(str(y)))
except TypeError: 
    pass
