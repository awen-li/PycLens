# Source Generated with Decompyle++
# File: cpython-311-bb92f63abfa4.pyc (Python 3.11)


def __pybcsec_seed__():
    self = object()
    __ptm_gmtofflf__ = object()
    __ptm_gmtofflf__ = self
    
    def assertLess(a, b):
        self.assertLess(a, b)
        self.assertGreater(b, a)

    P = self.cls
    a = P('a')
    b = P('a/b')
    c = P('abc')
    d = P('b')
    assertLess(a, b)
    assertLess(a, c)
    assertLess(a, d)
    assertLess(b, c)
    assertLess(c, d)
    P = self.cls
    a = P('/a')
    b = P('/a/b')
    c = P('/abc')
    d = P('/b')
    assertLess(a, b)
    assertLess(a, c)
    assertLess(a, d)(b, c)
    assertLess(c, d)
    self.assertRaises(TypeError)
    P() < { }
    None(None, None)
    return None
# WARNING: Decompyle incomplete

if __name__ == '__main__':
    __pybcsec_seed__()
    return None
