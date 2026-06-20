# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: AllTests_test_all

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from typing import __all__ as a
    self.assertIn('AbstractSet', a)
    self.assertIn('ValuesView', a)
    self.assertIn('cast', a)
    self.assertIn('overload', a)
    self.assertIn('ContextManager', a)
    self.assertIn('AsyncContextManager', a)
    self.assertNotIn('io', a)
    self.assertNotIn('re', a)
    self.assertNotIn('os', a)
    self.assertNotIn('sys', a)
    self.assertIn('Text', a)
    self.assertIn('SupportsBytes', a)
    self.assertIn('SupportsComplex', a)
