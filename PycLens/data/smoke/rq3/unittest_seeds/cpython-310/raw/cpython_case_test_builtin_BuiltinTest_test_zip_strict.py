# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_zip_strict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(tuple(zip((1, 2, 3), 'abc', strict=True)), ((1, 'a'), (2, 'b'), (3, 'c')))
    self.assertRaises(ValueError, tuple, zip((1, 2, 3, 4), 'abc', strict=True))
    self.assertRaises(ValueError, tuple, zip((1, 2), 'abc', strict=True))
    self.assertRaises(ValueError, tuple, zip((1, 2), (1, 2), 'abc', strict=True))
