# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestInterpreterStack_test_frame

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (args, varargs, varkw, locals) = inspect.getargvalues(mod.fr)
    self.assertEqual(args, ['x', 'y'])
    self.assertEqual(varargs, None)
    self.assertEqual(varkw, None)
    self.assertEqual(locals, {'x': 11, 'p': 11, 'y': 14})
    self.assertEqual(inspect.formatargvalues(args, varargs, varkw, locals), '(x=11, y=14)')
