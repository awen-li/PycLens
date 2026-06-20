# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_marshal.py
# case: BugsTestCase_test_patch_873224

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(Exception, marshal.loads, b'0')
    self.assertRaises(Exception, marshal.loads, b'f')
    self.assertRaises(Exception, marshal.loads, marshal.dumps(2 ** 65)[:-1])
