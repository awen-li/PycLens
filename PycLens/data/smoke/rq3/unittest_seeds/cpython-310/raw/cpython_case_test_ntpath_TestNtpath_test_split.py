# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ntpath.py
# case: TestNtpath_test_split

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tester('ntpath.split("c:\\foo\\bar")', ('c:\\foo', 'bar'))
    tester('ntpath.split("\\\\conky\\mountpoint\\foo\\bar")', ('\\\\conky\\mountpoint\\foo', 'bar'))
    tester('ntpath.split("c:\\")', ('c:\\', ''))
    tester('ntpath.split("\\\\conky\\mountpoint\\")', ('\\\\conky\\mountpoint\\', ''))
    tester('ntpath.split("c:/")', ('c:/', ''))
    tester('ntpath.split("//conky/mountpoint/")', ('//conky/mountpoint/', ''))
