# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_listcomps_test_nested_front

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual([[y for y in [x, x + 1]] for x in [1, 3, 5]], [[1, 2], [3, 4], [5, 6]])
