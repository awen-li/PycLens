# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: PurePosixPathTest_test_as_uri

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    self.assertEqual(P('/').as_uri(), 'file:///')
    self.assertEqual(P('/a/b.c').as_uri(), 'file:///a/b.c')
    self.assertEqual(P('/a/b%#c').as_uri(), 'file:///a/b%25%23c')
