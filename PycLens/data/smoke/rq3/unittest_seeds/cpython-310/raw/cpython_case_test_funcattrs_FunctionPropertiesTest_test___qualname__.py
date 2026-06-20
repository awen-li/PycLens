# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_funcattrs.py
# case: FunctionPropertiesTest_test___qualname__

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self.b.__qualname__, 'FuncAttrsTest.setUp.<locals>.b')
    self.assertEqual(FuncAttrsTest.setUp.__qualname__, 'FuncAttrsTest.setUp')
    self.assertEqual(global_function.__qualname__, 'global_function')
    self.assertEqual(global_function().__qualname__, 'global_function.<locals>.<lambda>')
    self.assertEqual(global_function()().__qualname__, 'global_function.<locals>.inner_function')
    self.assertEqual(global_function()()().__qualname__, 'global_function.<locals>.inner_function.<locals>.LocalClass')
    self.assertEqual(inner_global_function.__qualname__, 'inner_global_function')
    self.assertEqual(inner_global_function().__qualname__, 'inner_global_function.<locals>.inner_function2')
    self.b.__qualname__ = 'c'
    self.assertEqual(self.b.__qualname__, 'c')
    self.b.__qualname__ = 'd'
    self.assertEqual(self.b.__qualname__, 'd')
    self.cannot_set_attr(self.b, '__qualname__', 7, TypeError)
