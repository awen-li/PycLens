# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_float.py
# case: IEEEFormatTestCase_test_serialized_float_rounding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from _testcapi import FLT_MAX
    self.assertEqual(struct.pack('<f', 3.40282356e+38), struct.pack('<f', FLT_MAX))
    self.assertEqual(struct.pack('<f', -3.40282356e+38), struct.pack('<f', -FLT_MAX))
