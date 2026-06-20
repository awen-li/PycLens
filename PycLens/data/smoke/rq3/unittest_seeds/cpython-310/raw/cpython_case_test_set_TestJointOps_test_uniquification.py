# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestJointOps_test_uniquification

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    actual = sorted(self.s)
    expected = sorted(self.d)
    self.assertEqual(actual, expected)
    self.assertRaises(PassThru, self.thetype, check_pass_thru())
    self.assertRaises(TypeError, self.thetype, [[]])
