# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePurePathTest_test_as_bytes_common

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sep = os.fsencode(self.sep)
    P = self.cls
    self.assertEqual(bytes(P('a/b')), b'a' + sep + b'b')
