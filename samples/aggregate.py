import collections.abc as abstract

# aggregation function which takes an optional mapping function and an optional filter function
# examples: 
# 
#   a = aggregate.aggregate([], "_wOof_", lambda x : str.isalnum(str(x)), lambda y : str.upper(str(y)))
#   assert("WOOF" == "".join(a))
#
#   b = aggregate.aggregate({}, "_woOf_", lambda x : str.isalnum(str(x)), lambda y : str.upper(str(y)))
#   assert("WOOF" == "".join(a))
#
def aggregate(container, iterable, filter_func=lambda _: True, mapper_func=lambda x: x):
    container_type_error = TypeError("container must be a mutable mapping or mutable sequence")
    if isinstance(iterable, abstract.Mapping):
        for k,v in iterable.items():
            if filter_func(v):
                if isinstance(container, abstract.MutableMapping):
                    container[k] = mapper_func(v)
                elif isinstance(container, abstract.MutableSequence):
                    container.append(mapper_func(v))
                else:
                    raise container_type_error
    else:
        for k,v in enumerate(iterable): # this may throw a TypeError if 'iterable' parameter is not iterable
            if filter_func(v):
                if isinstance(container, abstract.MutableMapping):
                    container[k] = mapper_func(v)
                elif isinstance(container, abstract.MutableSequence):
                    container.append(mapper_func(v))
                else:
                    raise container_type_error

    return container

