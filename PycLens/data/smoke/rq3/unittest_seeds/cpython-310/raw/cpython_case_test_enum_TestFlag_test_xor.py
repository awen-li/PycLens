# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestFlag_test_xor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Perm = self.Perm
    for i in Perm:
        for j in Perm:
            self.assertEqual((i ^ j).value, i.value ^ j.value)
            self.assertIs(type(i ^ j), Perm)
    for i in Perm:
        self.assertIs(i ^ Perm(0), i)
        self.assertIs(Perm(0) ^ i, i)
    Open = self.Open
    self.assertIs(Open.RO ^ Open.CE, Open.CE)
    self.assertIs(Open.CE ^ Open.CE, Open.RO)
