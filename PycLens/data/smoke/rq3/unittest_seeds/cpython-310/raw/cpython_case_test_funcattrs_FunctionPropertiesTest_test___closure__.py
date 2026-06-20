# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_funcattrs.py
# case: FunctionPropertiesTest_test___closure__

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = 12

    def f():
        print(a)
    c = f.__closure__
    self.assertIsInstance(c, tuple)
    self.assertEqual(len(c), 1)
    self.assertEqual(c[0].__class__.__name__, 'cell')
    self.cannot_set_attr(f, '__closure__', c, AttributeError)
