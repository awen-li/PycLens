# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_while

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    while 0:
        pass
    while 0:
        pass
    else:
        pass
    x = 0
    while 0:
        x = 1
    else:
        x = 2
    self.assertEqual(x, 2)
