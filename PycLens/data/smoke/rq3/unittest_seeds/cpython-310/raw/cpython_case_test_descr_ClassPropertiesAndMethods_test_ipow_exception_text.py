# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_ipow_exception_text

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = None
    with self.assertRaises(TypeError) as cm:
        x **= 2
    self.assertIn('unsupported operand type(s) for **=', str(cm.exception))
    with self.assertRaises(TypeError) as cm:
        y = x ** 2
    self.assertIn('unsupported operand type(s) for **', str(cm.exception))
