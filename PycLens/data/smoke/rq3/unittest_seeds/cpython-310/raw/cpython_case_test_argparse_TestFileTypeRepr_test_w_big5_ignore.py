# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestFileTypeRepr_test_w_big5_ignore

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    type = argparse.FileType('w', encoding='big5', errors='ignore')
    self.assertEqual("FileType('w', encoding='big5', errors='ignore')", repr(type))
