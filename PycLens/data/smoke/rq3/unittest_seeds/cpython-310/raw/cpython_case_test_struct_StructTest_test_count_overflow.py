# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_struct.py
# case: StructTest_test_count_overflow

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    hugecount = '{}b'.format(sys.maxsize + 1)
    self.assertRaises(struct.error, struct.calcsize, hugecount)
    hugecount2 = '{}b{}H'.format(sys.maxsize // 2, sys.maxsize // 2)
    self.assertRaises(struct.error, struct.calcsize, hugecount2)
