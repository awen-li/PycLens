# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_syntax.py
# case: SyntaxTestCase_test_break_outside_loop

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = 'outside loop'
    self._check_error('break', msg, lineno=1)
    self._check_error('if 0: break', msg, lineno=1)
    self._check_error('if 0: break\nelse:  x=1', msg, lineno=1)
    self._check_error('if 1: pass\nelse: break', msg, lineno=2)
    self._check_error('class C:\n  if 0: break', msg, lineno=2)
    self._check_error('class C:\n  if 1: pass\n  else: break', msg, lineno=3)
    self._check_error('with object() as obj:\n break', msg, lineno=2)
