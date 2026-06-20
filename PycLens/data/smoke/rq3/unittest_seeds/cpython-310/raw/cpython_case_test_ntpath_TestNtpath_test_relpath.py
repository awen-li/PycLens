# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ntpath.py
# case: TestNtpath_test_relpath

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tester('ntpath.relpath("a")', 'a')
    tester('ntpath.relpath(ntpath.abspath("a"))', 'a')
    tester('ntpath.relpath("a/b")', 'a\\b')
    tester('ntpath.relpath("../a/b")', '..\\a\\b')
    with os_helper.temp_cwd(os_helper.TESTFN) as cwd_dir:
        currentdir = ntpath.basename(cwd_dir)
        tester('ntpath.relpath("a", "../b")', '..\\' + currentdir + '\\a')
        tester('ntpath.relpath("a/b", "../c")', '..\\' + currentdir + '\\a\\b')
    tester('ntpath.relpath("a", "b/c")', '..\\..\\a')
    tester('ntpath.relpath("c:/foo/bar/bat", "c:/x/y")', '..\\..\\foo\\bar\\bat')
    tester('ntpath.relpath("//conky/mountpoint/a", "//conky/mountpoint/b/c")', '..\\..\\a')
    tester('ntpath.relpath("a", "a")', '.')
    tester('ntpath.relpath("/foo/bar/bat", "/x/y/z")', '..\\..\\..\\foo\\bar\\bat')
    tester('ntpath.relpath("/foo/bar/bat", "/foo/bar")', 'bat')
    tester('ntpath.relpath("/foo/bar/bat", "/")', 'foo\\bar\\bat')
    tester('ntpath.relpath("/", "/foo/bar/bat")', '..\\..\\..')
    tester('ntpath.relpath("/foo/bar/bat", "/x")', '..\\foo\\bar\\bat')
    tester('ntpath.relpath("/x", "/foo/bar/bat")', '..\\..\\..\\x')
    tester('ntpath.relpath("/", "/")', '.')
    tester('ntpath.relpath("/a", "/a")', '.')
    tester('ntpath.relpath("/a/b", "/a/b")', '.')
    tester('ntpath.relpath("c:/foo", "C:/FOO")', '.')
