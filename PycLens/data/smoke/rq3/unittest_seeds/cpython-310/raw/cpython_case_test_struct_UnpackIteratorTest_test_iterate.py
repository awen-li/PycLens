# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_struct.py
# case: UnpackIteratorTest_test_iterate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = struct.Struct('>IB')
    b = bytes(range(1, 16))
    it = s.iter_unpack(b)
    self.assertEqual(next(it), (16909060, 5))
    self.assertEqual(next(it), (101124105, 10))
    self.assertEqual(next(it), (185339150, 15))
    self.assertRaises(StopIteration, next, it)
    self.assertRaises(StopIteration, next, it)
