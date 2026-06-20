# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestBasicOps_test_chain

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def chain2(*iterables):
        """Pure python version in the docs"""
        for it in iterables:
            for element in it:
                yield element
    for c in (chain, chain2):
        self.assertEqual(list(c('abc', 'def')), list('abcdef'))
        self.assertEqual(list(c('abc')), list('abc'))
        self.assertEqual(list(c('')), [])
        self.assertEqual(take(4, c('abc', 'def')), list('abcd'))
        self.assertRaises(TypeError, list, c(2, 3))
