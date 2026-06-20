# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: PurePathTest_test_different_flavours_unordered

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = pathlib.PurePosixPath('a')
    q = pathlib.PureWindowsPath('a')
    with self.assertRaises(TypeError):
        p < q
    with self.assertRaises(TypeError):
        p <= q
    with self.assertRaises(TypeError):
        p > q
    with self.assertRaises(TypeError):
        p >= q
