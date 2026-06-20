# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_module.py
# case: ModuleTests_test_ascii_docstring

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    foo = ModuleType('foo', 'foodoc')
    self.assertEqual(foo.__name__, 'foo')
    self.assertEqual(foo.__doc__, 'foodoc')
    self.assertEqual(foo.__dict__, {'__name__': 'foo', '__doc__': 'foodoc', '__loader__': None, '__package__': None, '__spec__': None})
