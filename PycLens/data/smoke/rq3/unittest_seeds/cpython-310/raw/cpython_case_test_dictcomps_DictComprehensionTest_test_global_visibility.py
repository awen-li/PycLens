# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dictcomps.py
# case: DictComprehensionTest_test_global_visibility

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected = {0: 'Global variable', 1: 'Global variable', 2: 'Global variable', 3: 'Global variable', 4: 'Global variable', 5: 'Global variable', 6: 'Global variable', 7: 'Global variable', 8: 'Global variable', 9: 'Global variable'}
    actual = {k: g for k in range(10)}
    self.assertEqual(actual, expected)
