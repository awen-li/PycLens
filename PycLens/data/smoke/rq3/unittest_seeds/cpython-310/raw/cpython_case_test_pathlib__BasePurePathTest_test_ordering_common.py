# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePurePathTest_test_ordering_common

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

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
    assertLess(a, d)
    assertLess(b, c)
    assertLess(c, d)
    with self.assertRaises(TypeError):
        P() < {}
