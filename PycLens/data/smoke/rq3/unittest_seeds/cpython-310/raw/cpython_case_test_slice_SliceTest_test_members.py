# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_slice.py
# case: SliceTest_test_members

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = slice(1)
    self.assertEqual(s.start, None)
    self.assertEqual(s.stop, 1)
    self.assertEqual(s.step, None)
    s = slice(1, 2)
    self.assertEqual(s.start, 1)
    self.assertEqual(s.stop, 2)
    self.assertEqual(s.step, None)
    s = slice(1, 2, 3)
    self.assertEqual(s.start, 1)
    self.assertEqual(s.stop, 2)
    self.assertEqual(s.step, 3)

    class AnyClass:
        pass
    obj = AnyClass()
    s = slice(obj)
    self.assertTrue(s.stop is obj)
