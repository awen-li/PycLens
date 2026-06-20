# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: TestSorted_test_inputtypes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = 'abracadabra'
    types = [list, tuple, str]
    for T in types:
        self.assertEqual(sorted(s), sorted(T(s)))
    s = ''.join(set(s))
    types = [str, set, frozenset, list, tuple, dict.fromkeys]
    for T in types:
        self.assertEqual(sorted(s), sorted(T(s)))
