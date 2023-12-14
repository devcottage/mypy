import aggregate 

mapper_func = lambda s : str.upper(str(s))
filter_func = lambda x : str.isalnum(str(x)) 

a = aggregate.aggregate([], "wOof_", filter_func, mapper_func)
assert("WOOF" == "".join(a))

b = aggregate.aggregate({}, "_wOof", filter_func, mapper_func)
assert("WOOF" == "".join(b.values()))

c = aggregate.aggregate({}, list("_woOf"), filter_func, mapper_func)
assert("WOOF" == "".join(c.values()))

d = aggregate.aggregate({}, dict(enumerate("_wOof")), filter_func, mapper_func)
assert("WOOF" == "".join(d.values()))

e = aggregate.aggregate({}, tuple("_woOf"), filter_func, mapper_func)
assert("WOOF" == "".join(e.values()))

f = aggregate.aggregate([], ['_','w','o','o','F'], filter_func, mapper_func)
assert("WOOF" == "".join(f))

g = aggregate.aggregate({}, set(['_','w','o','O','f']), filter_func, mapper_func)
assert("WOOF" == "".join(sorted(g.values(), reverse=True)))

try:
    aggregate.aggregate(tuple(), set(['_','w','o','O','f']), filter_func, mapper_func)
except TypeError as ex:
    expected_msg = "Container must be a mutable mapping or mutable sequence"
    assert str(ex).lower() == expected_msg.lower(), f"expected: \"{expected_msg}\""

try:
    aggregate.aggregate(tuple(), None, filter_func, mapper_func)
except TypeError as ex:
    expected_msg = "'NoneType' object is not iterable"
    assert str(ex).lower() == expected_msg.lower(), f"expected: \"{expected_msg}\""

print("DONE testing aggregation")
