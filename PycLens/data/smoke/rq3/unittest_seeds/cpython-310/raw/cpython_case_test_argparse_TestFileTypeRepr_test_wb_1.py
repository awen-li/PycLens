# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestFileTypeRepr_test_wb_1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    type = argparse.FileType('wb', 1)
    self.assertEqual("FileType('wb', 1)", repr(type))
