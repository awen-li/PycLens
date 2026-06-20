# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: PathTest_test_concrete_class

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = self.cls('a')
    self.assertIs(type(p), pathlib.WindowsPath if os.name == 'nt' else pathlib.PosixPath)
