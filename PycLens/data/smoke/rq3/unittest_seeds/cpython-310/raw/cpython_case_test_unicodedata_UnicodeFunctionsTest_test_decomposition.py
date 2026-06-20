# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicodedata.py
# case: UnicodeFunctionsTest_test_decomposition

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self.db.decomposition('\ufffe'), '')
    self.assertEqual(self.db.decomposition('¼'), '<fraction> 0031 2044 0034')
    self.assertRaises(TypeError, self.db.decomposition)
    self.assertRaises(TypeError, self.db.decomposition, 'xx')
