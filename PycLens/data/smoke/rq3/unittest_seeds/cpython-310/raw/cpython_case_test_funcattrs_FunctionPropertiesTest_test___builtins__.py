# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_funcattrs.py
# case: FunctionPropertiesTest_test___builtins__

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIs(self.b.__builtins__, __builtins__)
    self.cannot_set_attr(self.b, '__builtins__', 2, (AttributeError, TypeError))

    def func(s):
        return len(s)
    ns = {}
    func2 = type(func)(func.__code__, ns)
    self.assertIs(func2.__globals__, ns)
    self.assertIs(func2.__builtins__, __builtins__)
    self.assertEqual(func2('abc'), 3)
    self.assertEqual(ns, {})
    code = textwrap.dedent('\n            def func3(s): pass\n            func4 = type(func3)(func3.__code__, {})\n        ')
    safe_builtins = {'None': None}
    ns = {'type': type, '__builtins__': safe_builtins}
    exec(code, ns)
    self.assertIs(ns['func3'].__builtins__, safe_builtins)
    self.assertIs(ns['func4'].__builtins__, safe_builtins)
    self.assertIs(ns['func3'].__globals__['__builtins__'], safe_builtins)
    self.assertNotIn('__builtins__', ns['func4'].__globals__)
