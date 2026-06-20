# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_future.py
# case: FutureTest_test_parserhack

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        exec('from __future__ import print_function; print 0')
    except SyntaxError:
        pass
    else:
        self.fail("syntax error didn't occur")
    try:
        exec('from __future__ import (print_function); print 0')
    except SyntaxError:
        pass
    else:
        self.fail("syntax error didn't occur")
