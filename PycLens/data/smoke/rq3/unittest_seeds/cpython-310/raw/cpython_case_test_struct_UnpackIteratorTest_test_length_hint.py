# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_struct.py
# case: UnpackIteratorTest_test_length_hint

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    lh = operator.length_hint
    s = struct.Struct('>IB')
    b = bytes(range(1, 16))
    it = s.iter_unpack(b)
    self.assertEqual(lh(it), 3)
    next(it)
    self.assertEqual(lh(it), 2)
    next(it)
    self.assertEqual(lh(it), 1)
    next(it)
    self.assertEqual(lh(it), 0)
    self.assertRaises(StopIteration, next, it)
    self.assertEqual(lh(it), 0)
