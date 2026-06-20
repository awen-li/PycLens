# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_timeit.py
# case: TestTimeit_test_timer_invalid_stmt

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(ValueError, timeit.Timer, stmt=None)
    self.assertRaises(SyntaxError, timeit.Timer, stmt='return')
    self.assertRaises(SyntaxError, timeit.Timer, stmt='yield')
    self.assertRaises(SyntaxError, timeit.Timer, stmt='yield from ()')
    self.assertRaises(SyntaxError, timeit.Timer, stmt='break')
    self.assertRaises(SyntaxError, timeit.Timer, stmt='continue')
    self.assertRaises(SyntaxError, timeit.Timer, stmt='from timeit import *')
    self.assertRaises(SyntaxError, timeit.Timer, stmt='  pass')
    self.assertRaises(SyntaxError, timeit.Timer, setup='while False:\n  pass', stmt='  break')
