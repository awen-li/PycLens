# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestFlag_test_bool

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Perm = self.Perm
    for f in Perm:
        self.assertTrue(f)
    Open = self.Open
    for f in Open:
        self.assertEqual(bool(f.value), bool(f))
