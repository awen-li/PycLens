# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dictcomps.py
# case: DictComprehensionTest_test_local_visibility

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    v = 'Local variable'
    expected = {0: 'Local variable', 1: 'Local variable', 2: 'Local variable', 3: 'Local variable', 4: 'Local variable', 5: 'Local variable', 6: 'Local variable', 7: 'Local variable', 8: 'Local variable', 9: 'Local variable'}
    actual = {k: v for k in range(10)}
    self.assertEqual(actual, expected)
    self.assertEqual(v, 'Local variable')
