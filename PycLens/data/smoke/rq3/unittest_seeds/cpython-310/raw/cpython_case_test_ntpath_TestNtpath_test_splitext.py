# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ntpath.py
# case: TestNtpath_test_splitext

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tester('ntpath.splitext("foo.ext")', ('foo', '.ext'))
    tester('ntpath.splitext("/foo/foo.ext")', ('/foo/foo', '.ext'))
    tester('ntpath.splitext(".ext")', ('.ext', ''))
    tester('ntpath.splitext("\\foo.ext\\foo")', ('\\foo.ext\\foo', ''))
    tester('ntpath.splitext("foo.ext\\")', ('foo.ext\\', ''))
    tester('ntpath.splitext("")', ('', ''))
    tester('ntpath.splitext("foo.bar.ext")', ('foo.bar', '.ext'))
    tester('ntpath.splitext("xx/foo.bar.ext")', ('xx/foo.bar', '.ext'))
    tester('ntpath.splitext("xx\\foo.bar.ext")', ('xx\\foo.bar', '.ext'))
    tester('ntpath.splitext("c:a/b\\c.d")', ('c:a/b\\c', '.d'))
