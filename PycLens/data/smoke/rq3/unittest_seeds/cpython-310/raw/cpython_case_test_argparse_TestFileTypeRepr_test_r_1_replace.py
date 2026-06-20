# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestFileTypeRepr_test_r_1_replace

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    type = argparse.FileType('r', 1, errors='replace')
    self.assertEqual("FileType('r', 1, errors='replace')", repr(type))
