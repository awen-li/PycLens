# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_hex_separator_five_bytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    five_bytes = self.type2test(range(90, 95))
    self.assertEqual(five_bytes.hex(), '5a5b5c5d5e')
