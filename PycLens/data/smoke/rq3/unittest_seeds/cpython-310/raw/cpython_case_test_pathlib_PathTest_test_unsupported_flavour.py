# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: PathTest_test_unsupported_flavour

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if os.name == 'nt':
        self.assertRaises(NotImplementedError, pathlib.PosixPath)
    else:
        self.assertRaises(NotImplementedError, pathlib.WindowsPath)
