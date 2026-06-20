# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestFlag_test_contains_tf

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Open = self.Open
    Color = self.Color
    self.assertFalse(Color.BLACK in Open)
    self.assertFalse(Open.RO in Color)
    self.assertFalse('BLACK' in Color)
    self.assertFalse('RO' in Open)
    self.assertTrue(1 in Color)
    self.assertTrue(1 in Open)
