# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestSpecifics_test_argument_handling

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(SyntaxError, eval, 'lambda a,a:0')
    self.assertRaises(SyntaxError, eval, 'lambda a,a=1:0')
    self.assertRaises(SyntaxError, eval, 'lambda a=1,a=1:0')
    self.assertRaises(SyntaxError, exec, 'def f(a, a): pass')
    self.assertRaises(SyntaxError, exec, 'def f(a = 0, a = 1): pass')
    self.assertRaises(SyntaxError, exec, 'def f(a): global a; a = 1')
