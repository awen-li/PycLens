# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_struct.py
# case: StructTest_test_format_attr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = struct.Struct('=i2H')
    self.assertEqual(s.format, '=i2H')
    s2 = struct.Struct(s.format.encode())
    self.assertEqual(s2.format, s.format)
