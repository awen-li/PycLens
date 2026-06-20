# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestFlag_test_or

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Perm = self.Perm
    for i in Perm:
        for j in Perm:
            self.assertEqual(i | j, Perm(i.value | j.value))
            self.assertEqual((i | j).value, i.value | j.value)
            self.assertIs(type(i | j), Perm)
    for i in Perm:
        self.assertIs(i | i, i)
    Open = self.Open
    self.assertIs(Open.RO | Open.CE, Open.CE)
