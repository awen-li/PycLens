# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestInterpreterStack_test_previous_frame

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (args, varargs, varkw, locals) = inspect.getargvalues(mod.fr.f_back)
    self.assertEqual(args, ['a', 'b', 'c', 'd', 'e', 'f'])
    self.assertEqual(varargs, 'g')
    self.assertEqual(varkw, 'h')
    self.assertEqual(inspect.formatargvalues(args, varargs, varkw, locals), '(a=7, b=8, c=9, d=3, e=4, f=5, *g=(), **h={})')
