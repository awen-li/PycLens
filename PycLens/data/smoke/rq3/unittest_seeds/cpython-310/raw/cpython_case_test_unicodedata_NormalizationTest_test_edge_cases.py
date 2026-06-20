# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicodedata.py
# case: NormalizationTest_test_edge_cases

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, unicodedata.normalize)
    self.assertRaises(ValueError, unicodedata.normalize, 'unknown', 'xx')
    self.assertEqual(unicodedata.normalize('NFKC', ''), '')
