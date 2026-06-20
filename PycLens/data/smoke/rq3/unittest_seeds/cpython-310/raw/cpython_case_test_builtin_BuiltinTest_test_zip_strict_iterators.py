# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_zip_strict_iterators

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = iter(range(5))
    y = [0]
    z = iter(range(5))
    self.assertRaises(ValueError, list, zip(x, y, z, strict=True))
    self.assertEqual(next(x), 2)
    self.assertEqual(next(z), 1)
