# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_from_list

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = self.type2test(list(range(256)))
    self.assertEqual(len(b), 256)
    self.assertEqual(list(b), list(range(256)))
    b = self.type2test([1, 2, 3])
    self.assertEqual(b, b'\x01\x02\x03')
