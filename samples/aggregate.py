# examples: 
#   a = aggregate([], "woof", lambda x : str.isalnum(str(x)), lambda y : str.upper(str(y)))
#   print("".join(a))
#
#   b = aggregate({}, "woof", lambda x : str.isalnum(str(x)), lambda y : str.upper(str(y)))
#   print("".join(b.values()))
#
import collections.abc as abstract
def aggregate(container, iterable, filt = lambda _ : True, map = lambda x : x):
    if isinstance(container, abstract.Iterable):
      for k,v in enumerate(iterable):
          if filt(v):
              if isinstance(container, abstract.Mapping):
                  container[k] = map(v)
              else:
                  container.append(map(v))
    return container
