# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_syntax.py
# case: SyntaxTestCase_test_return_outside_function

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._check_error('if 0: return', 'outside function')
    self._check_error('if 0: return\nelse:  x=1', 'outside function')
    self._check_error('if 1: pass\nelse: return', 'outside function')
    self._check_error('while 0: return', 'outside function')
    self._check_error('class C:\n  if 0: return', 'outside function')
    self._check_error('class C:\n  while 0: return', 'outside function')
    self._check_error('class C:\n  while 0: return\n  else:  x=1', 'outside function')
    self._check_error('class C:\n  if 0: return\n  else: x= 1', 'outside function')
    self._check_error('class C:\n  if 1: pass\n  else: return', 'outside function')
