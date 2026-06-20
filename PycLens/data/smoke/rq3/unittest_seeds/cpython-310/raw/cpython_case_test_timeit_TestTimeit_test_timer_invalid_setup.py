# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_timeit.py
# case: TestTimeit_test_timer_invalid_setup

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(ValueError, timeit.Timer, setup=None)
    self.assertRaises(SyntaxError, timeit.Timer, setup='return')
    self.assertRaises(SyntaxError, timeit.Timer, setup='yield')
    self.assertRaises(SyntaxError, timeit.Timer, setup='yield from ()')
    self.assertRaises(SyntaxError, timeit.Timer, setup='break')
    self.assertRaises(SyntaxError, timeit.Timer, setup='continue')
    self.assertRaises(SyntaxError, timeit.Timer, setup='from timeit import *')
    self.assertRaises(SyntaxError, timeit.Timer, setup='  pass')
