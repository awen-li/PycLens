# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestIntFlag_test_member_contains

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Perm = self.Perm
    (R, W, X) = Perm
    RW = R | W
    RX = R | X
    WX = W | X
    RWX = R | W | X
    self.assertTrue(R in RW)
    self.assertTrue(R in RX)
    self.assertTrue(R in RWX)
    self.assertTrue(W in RW)
    self.assertTrue(W in WX)
    self.assertTrue(W in RWX)
    self.assertTrue(X in RX)
    self.assertTrue(X in WX)
    self.assertTrue(X in RWX)
    self.assertFalse(R in WX)
    self.assertFalse(W in RX)
    self.assertFalse(X in RW)
    with self.assertRaises(TypeError):
        self.assertFalse('test' in RW)
