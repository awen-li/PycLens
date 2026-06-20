# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_integer_arguments_out_of_byte_range

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = self.type2test(b'hello')
    for method in (b.count, b.find, b.index, b.rfind, b.rindex):
        self.assertRaises(ValueError, method, -1)
        self.assertRaises(ValueError, method, 256)
        self.assertRaises(ValueError, method, 9999)
