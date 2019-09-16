from itertools import chain, combinations_with_replacement

def powerset(iterable):
    s = list(iterable)
    return list(chain.from_iterable(combinations_with_replacement(s, r) for r in range(len(s)+1)))

def array_equals(a, b):
    if len(a)==len(b)==0:
        return True
    if a[0]!=b[0] or len(a)!=len(b):
        return False

    return array_equals(a[1:], b[1:])
    
