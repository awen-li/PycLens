# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigmem.py
# case: TupleTest_test_index_and_slice

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t = (None,) * size
    self.assertEqual(len(t), size)
    self.assertEqual(t[-1], None)
    self.assertEqual(t[5], None)
    self.assertEqual(t[size - 1], None)
    self.assertRaises(IndexError, operator.getitem, t, size)
    self.assertEqual(t[:5], (None,) * 5)
    self.assertEqual(t[-5:], (None,) * 5)
    self.assertEqual(t[20:25], (None,) * 5)
    self.assertEqual(t[-25:-20], (None,) * 5)
    self.assertEqual(t[size - 5:], (None,) * 5)
    self.assertEqual(t[size - 5:size], (None,) * 5)
    self.assertEqual(t[size - 6:size - 2], (None,) * 4)
    self.assertEqual(t[size:size], ())
    self.assertEqual(t[size:size + 5], ())
