# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestFrozenSet_test_frozen_as_dictkey

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    seq = list(range(10)) + list('abcdefg') + ['apple']
    key1 = self.thetype(seq)
    key2 = self.thetype(reversed(seq))
    self.assertEqual(key1, key2)
    self.assertNotEqual(id(key1), id(key2))
    d = {}
    d[key1] = 42
    self.assertEqual(d[key2], 42)
