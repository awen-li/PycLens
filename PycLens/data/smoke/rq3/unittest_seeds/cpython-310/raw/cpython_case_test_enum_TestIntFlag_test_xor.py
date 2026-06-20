# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestIntFlag_test_xor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Perm = self.Perm
    for i in Perm:
        for j in Perm:
            self.assertEqual(i ^ j, i.value ^ j.value)
            self.assertEqual((i ^ j).value, i.value ^ j.value)
            self.assertIs(type(i ^ j), Perm)
        for j in range(8):
            self.assertEqual(i ^ j, i.value ^ j)
            self.assertEqual((i ^ j).value, i.value ^ j)
            self.assertIs(type(i ^ j), Perm)
            self.assertEqual(j ^ i, j ^ i.value)
            self.assertEqual((j ^ i).value, j ^ i.value)
            self.assertIs(type(j ^ i), Perm)
    for i in Perm:
        self.assertIs(i ^ 0, i)
        self.assertIs(0 ^ i, i)
    Open = self.Open
    self.assertIs(Open.RO ^ Open.CE, Open.CE)
    self.assertIs(Open.CE ^ Open.CE, Open.RO)
