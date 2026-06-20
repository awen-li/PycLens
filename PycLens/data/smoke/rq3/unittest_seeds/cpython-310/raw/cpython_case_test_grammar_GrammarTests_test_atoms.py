# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_atoms

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = 1
    x = 1 or 2 or 3
    x = (1 or 2 or 3, 2, 3)
    x = []
    x = [1]
    x = [1 or 2 or 3]
    x = [1 or 2 or 3, 2, 3]
    x = []
    x = {}
    x = {'one': 1}
    x = {'one': 1}
    x = {'one' or 'two': 1 or 2}
    x = {'one': 1, 'two': 2}
    x = {'one': 1, 'two': 2}
    x = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6}
    x = {'one'}
    x = {'one', 1}
    x = {'one', 'two', 'three'}
    x = {2, 3, 4}
    x = x
    x = 'x'
    x = 123
