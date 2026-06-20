# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestIntFlag_test_invert

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Perm = self.Perm
    RW = Perm.R | Perm.W
    RX = Perm.R | Perm.X
    WX = Perm.W | Perm.X
    RWX = Perm.R | Perm.W | Perm.X
    values = list(Perm) + [RW, RX, WX, RWX, Perm(0)]
    for i in values:
        self.assertEqual(~i, ~i.value)
        self.assertEqual((~i).value, ~i.value)
        self.assertIs(type(~i), Perm)
        self.assertEqual(~~i, i)
    for i in Perm:
        self.assertIs(~~i, i)
    Open = self.Open
    self.assertIs(Open.WO & ~Open.WO, Open.RO)
    self.assertIs((Open.WO | Open.CE) & ~Open.WO, Open.CE)
