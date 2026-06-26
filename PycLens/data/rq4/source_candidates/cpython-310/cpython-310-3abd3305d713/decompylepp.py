# Source Generated with Decompyle++
# File: cpython-310-3abd3305d713.pyc (Python 3.10)


def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    
    class C(object):
        
        def __imul__(self, other):
            return (self, other)


    x = C()
    y = x
    y *= 1
    self.assertEqual(y, (x, 1))
    y = x
    y *= 2
    self.assertEqual(y, (x, 2))
    y = x
    y *= 3
    self.assertEqual(y, (x, 3))
    y = x
    y *= 0x10000000000000000000000000
    self.assertEqual(y, (x, 0x10000000000000000000000000))
    y = x
    y *= None
    self.assertEqual(y, (x, None))
    y = x
    y *= 'foo'
    self.assertEqual(y, (x, 'foo'))

if __name__ == '__main__':
    __pybcsec_seed__()
    return None
