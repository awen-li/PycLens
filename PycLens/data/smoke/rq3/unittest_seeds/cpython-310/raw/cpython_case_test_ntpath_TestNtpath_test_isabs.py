# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ntpath.py
# case: TestNtpath_test_isabs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tester('ntpath.isabs("c:\\")', 1)
    tester('ntpath.isabs("\\\\conky\\mountpoint\\")', 1)
    tester('ntpath.isabs("\\foo")', 1)
    tester('ntpath.isabs("\\foo\\bar")', 1)
