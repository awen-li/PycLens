# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: PurePosixPathTest_test_is_reserved

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    self.assertIs(False, P('').is_reserved())
    self.assertIs(False, P('/').is_reserved())
    self.assertIs(False, P('/foo/bar').is_reserved())
    self.assertIs(False, P('/dev/con/PRN/NUL').is_reserved())
