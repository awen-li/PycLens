# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_struct.py
# case: StructTest_test_1530559

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (code, byteorder) in iter_integer_formats():
        format = byteorder + code
        self.assertRaises(struct.error, struct.pack, format, 1.0)
        self.assertRaises(struct.error, struct.pack, format, 1.5)
    self.assertRaises(struct.error, struct.pack, 'P', 1.0)
    self.assertRaises(struct.error, struct.pack, 'P', 1.5)
