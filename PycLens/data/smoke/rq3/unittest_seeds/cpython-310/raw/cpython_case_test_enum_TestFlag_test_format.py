# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestFlag_test_format

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Perm = self.Perm
    self.assertEqual(format(Perm.R, ''), 'Perm.R')
    self.assertEqual(format(Perm.R | Perm.X, ''), 'Perm.R|X')
