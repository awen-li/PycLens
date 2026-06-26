# Source Generated with Decompyle++
# File: cpython-312-056e0268a396.pyc (Python 3.12)


def __pybcsec_seed__():
    self = object()
    __pybcsec_self__ = object()
    __pybcsec_self__ = self
    
    class Class:
        __slots__ = None

    
    def Sneaky():
        '''__pybcsec_seed__.<locals>.Sneaky'''
        __slots__ = ('shadowed',)
        shadowing = <NODE:36>.slot

    Sneaky = None(Sneaky, 'Sneaky')
    
    def f(o):
        o.shadowing = 42

    o = Sneaky()
    for _ in range(1025):
        self.assertRaises(TypeError)
        f(o)
        None(None, None)
    return None
    if None:
        pass
    with None:
        if not None:
            pass
    continue

if __name__ == '__main__':
    __pybcsec_seed__()
    return None
