# examples: 
# 
#   a = aggregate.aggregate([], "woof", lambda x : str.isalnum(str(x)), lambda y : str.upper(str(y)))
#   print("".join(a))
#
#   b = aggregate.aggregate({}, "woof", lambda x : str.isalnum(str(x)), lambda y : str.upper(str(y)))
#   print("".join(b.values()))
#
import collections.abc as abstract

def aggregate(container, iterable, filt = lambda _ : True, map = lambda x : x):
    if isinstance(container, abstract.Iterable):
      for k,v in enumerate(iterable):
          if filt(v):
              if isinstance(container, abstract.MutableMapping):
                  container[k] = map(v)
              elif isinstance(container, abstract.MutableSequence):
                  container.append(map(v))
              else:
                  raise TypeError("container must be a mutable mapping or sequence")
    return container
