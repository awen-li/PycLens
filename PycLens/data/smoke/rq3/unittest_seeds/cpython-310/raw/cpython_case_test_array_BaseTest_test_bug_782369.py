# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: BaseTest_test_bug_782369

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for i in range(10):
        b = array.array('B', range(64))
    rc = sys.getrefcount(10)
    for i in range(10):
        b = array.array('B', range(64))
    self.assertEqual(rc, sys.getrefcount(10))
