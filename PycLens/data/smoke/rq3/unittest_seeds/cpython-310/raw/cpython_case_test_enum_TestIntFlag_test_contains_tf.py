# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestIntFlag_test_contains_tf

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Open = self.Open
    Color = self.Color
    self.assertTrue(Color.GREEN in Color)
    self.assertTrue(Open.RW in Open)
    self.assertTrue(Color.GREEN in Open)
    self.assertTrue(Open.RW in Color)
    self.assertFalse('GREEN' in Color)
    self.assertFalse('RW' in Open)
    self.assertTrue(2 in Color)
    self.assertTrue(2 in Open)
