# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: PureWindowsPathTest_test_ordering_common

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def assertOrderedEqual(a, b):
        self.assertLessEqual(a, b)
        self.assertGreaterEqual(b, a)
    P = self.cls
    p = P('c:A/b')
    q = P('C:a/B')
    assertOrderedEqual(p, q)
    self.assertFalse(p < q)
    self.assertFalse(p > q)
    p = P('//some/Share/A/b')
    q = P('//Some/SHARE/a/B')
    assertOrderedEqual(p, q)
    self.assertFalse(p < q)
    self.assertFalse(p > q)
