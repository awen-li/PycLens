# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestIntFlag_test_type

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Perm = self.Perm
    self.assertTrue(Perm._member_type_ is int)
    Open = self.Open
    for f in Perm:
        self.assertTrue(isinstance(f, Perm))
        self.assertEqual(f, f.value)
    self.assertTrue(isinstance(Perm.W | Perm.X, Perm))
    self.assertEqual(Perm.W | Perm.X, 3)
    for f in Open:
        self.assertTrue(isinstance(f, Open))
        self.assertEqual(f, f.value)
    self.assertTrue(isinstance(Open.WO | Open.RW, Open))
    self.assertEqual(Open.WO | Open.RW, 3)
