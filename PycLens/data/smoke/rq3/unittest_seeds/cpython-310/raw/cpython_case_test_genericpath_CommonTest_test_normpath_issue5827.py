# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericpath.py
# case: CommonTest_test_normpath_issue5827

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for path in ('', '.', '/', '\\', '///foo/.//bar//'):
        self.assertIsInstance(self.pathmodule.normpath(path), str)
