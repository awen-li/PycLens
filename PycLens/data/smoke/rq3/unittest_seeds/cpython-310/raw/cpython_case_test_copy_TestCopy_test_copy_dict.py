# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_copy.py
# case: TestCopy_test_copy_dict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = {'foo': 1, 'bar': 2}
    y = copy.copy(x)
    self.assertEqual(y, x)
    self.assertIsNot(y, x)
    x = {}
    y = copy.copy(x)
    self.assertEqual(y, x)
    self.assertIsNot(y, x)
