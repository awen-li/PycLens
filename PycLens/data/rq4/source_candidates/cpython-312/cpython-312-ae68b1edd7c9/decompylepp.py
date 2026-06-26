# Source Generated with Decompyle++
# File: cpython-312-ae68b1edd7c9.pyc (Python 3.12)


def __pybcsec_seed__():
    self = object()
    __pybcsec_self__ = object()
    __pybcsec_self__ = self
    HAS_MORE = 1
    NO_MORE = 2
    
    def exhaust(iterator):
        '''Exhaust an iterator without raising StopIteration.'''
        list(iterator)

    
    def spam():
        if spam.is_recursive_call:
            return NO_MORE
        spam.is_recursive_call = None
        exhaust(spam.iterator)
        return HAS_MORE

    spam.is_recursive_call = False
    spam.iterator = iter(spam, NO_MORE)
    self.assertRaises(StopIteration)
    next(spam.iterator)
    None(None, None)
    return None
    if None:
        pass
    with None:
        if not None:
            pass

if __name__ == '__main__':
    __pybcsec_seed__()
    return None
