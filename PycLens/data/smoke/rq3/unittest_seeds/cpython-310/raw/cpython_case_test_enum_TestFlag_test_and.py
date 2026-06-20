# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestFlag_test_and

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
        for j in values:
            self.assertEqual((i & j).value, i.value & j.value)
            self.assertIs(type(i & j), Perm)
    for i in Perm:
        self.assertIs(i & i, i)
        self.assertIs(i & RWX, i)
        self.assertIs(RWX & i, i)
    Open = self.Open
    self.assertIs(Open.RO & Open.CE, Open.RO)
