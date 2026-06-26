# Source Generated with Decompyle++
# File: cpython-310-09ede1f2a7d5.pyc (Python 3.10)


def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    
    class Foo:
        pass

    Foo = None
    None <<= None
    foo = Foo()
    self.assertRaises(RecursionError, str, foo)
    self.assertRaises(RecursionError, repr, foo)

if __name__ == '__main__':
    __pybcsec_seed__()
    return None
