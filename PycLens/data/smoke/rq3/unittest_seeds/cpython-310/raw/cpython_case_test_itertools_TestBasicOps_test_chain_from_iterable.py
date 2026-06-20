# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestBasicOps_test_chain_from_iterable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(list(chain.from_iterable(['abc', 'def'])), list('abcdef'))
    self.assertEqual(list(chain.from_iterable(['abc'])), list('abc'))
    self.assertEqual(list(chain.from_iterable([''])), [])
    self.assertEqual(take(4, chain.from_iterable(['abc', 'def'])), list('abcd'))
    self.assertRaises(TypeError, list, chain.from_iterable([2, 3]))
