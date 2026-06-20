# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_marshal.py
# case: BugsTestCase_test_version_argument

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(marshal.loads(marshal.dumps(5, 0)), 5)
    self.assertEqual(marshal.loads(marshal.dumps(5, 1)), 5)
