# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_dictcomps

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    nums = [1, 2, 3]
    self.assertEqual({i: i + 1 for i in nums}, {1: 2, 2: 3, 3: 4})
