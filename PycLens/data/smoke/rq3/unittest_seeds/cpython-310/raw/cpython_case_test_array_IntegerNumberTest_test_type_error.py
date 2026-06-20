# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: IntegerNumberTest_test_type_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = array.array(self.typecode)
    a.append(42)
    with self.assertRaises(TypeError):
        a.append(42.0)
    with self.assertRaises(TypeError):
        a[0] = 42.0
