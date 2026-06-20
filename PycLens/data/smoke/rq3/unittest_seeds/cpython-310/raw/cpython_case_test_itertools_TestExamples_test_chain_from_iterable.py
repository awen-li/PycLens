# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestExamples_test_chain_from_iterable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(''.join(chain.from_iterable(['ABC', 'DEF'])), 'ABCDEF')
