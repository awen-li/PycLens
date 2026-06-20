# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmath.py
# case: CMathTests_test_input_type

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for f in self.test_functions:
        for arg in [2, 2.0]:
            self.assertEqual(f(arg), f(arg.__float__()))
    for f in self.test_functions:
        for arg in ['a', 'long_string', '0', '1j', '']:
            self.assertRaises(TypeError, f, arg)
