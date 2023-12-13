import collections.abc as abstract


# examples: 
# 
#   a = aggregate.aggregate([], "woof", lambda x : str.isalnum(str(x)), lambda y : str.upper(str(y)))
#   print("".join(a))
#
#   b = aggregate.aggregate({}, "woof", lambda x : str.isalnum(str(x)), lambda y : str.upper(str(y)))
#   print("".join(b.values()))
#
def aggregate(container, iterable, filter_func=lambda _: True, mapper_func=lambda x: x):
    for k, v in enumerate(iterable):
        if filter_func(v):
            if isinstance(container, abstract.MutableMapping):
                container[k] = mapper_func(v)
            elif isinstance(container, abstract.MutableSequence):
                container.append(mapper_func(v))
            else:
                raise TypeError("container must be a mutable mapping or mutable sequence")
    return container
