# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestJointOps_test_badcmp

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = self.thetype([BadCmp()])
    self.assertRaises(RuntimeError, self.thetype, [BadCmp(), BadCmp()])
    self.assertRaises(RuntimeError, s.__contains__, BadCmp())
    if hasattr(s, 'add'):
        self.assertRaises(RuntimeError, s.add, BadCmp())
        self.assertRaises(RuntimeError, s.discard, BadCmp())
        self.assertRaises(RuntimeError, s.remove, BadCmp())
