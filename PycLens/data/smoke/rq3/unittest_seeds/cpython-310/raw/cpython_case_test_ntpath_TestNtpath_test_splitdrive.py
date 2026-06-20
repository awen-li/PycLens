# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ntpath.py
# case: TestNtpath_test_splitdrive

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tester('ntpath.splitdrive("c:\\foo\\bar")', ('c:', '\\foo\\bar'))
    tester('ntpath.splitdrive("c:/foo/bar")', ('c:', '/foo/bar'))
    tester('ntpath.splitdrive("\\\\conky\\mountpoint\\foo\\bar")', ('\\\\conky\\mountpoint', '\\foo\\bar'))
    tester('ntpath.splitdrive("//conky/mountpoint/foo/bar")', ('//conky/mountpoint', '/foo/bar'))
    tester('ntpath.splitdrive("\\\\\\conky\\mountpoint\\foo\\bar")', ('', '\\\\\\conky\\mountpoint\\foo\\bar'))
    tester('ntpath.splitdrive("///conky/mountpoint/foo/bar")', ('', '///conky/mountpoint/foo/bar'))
    tester('ntpath.splitdrive("\\\\conky\\\\mountpoint\\foo\\bar")', ('', '\\\\conky\\\\mountpoint\\foo\\bar'))
    tester('ntpath.splitdrive("//conky//mountpoint/foo/bar")', ('', '//conky//mountpoint/foo/bar'))
    self.assertEqual(ntpath.splitdrive('//conky/MOUNTPOİNT/foo/bar'), ('//conky/MOUNTPOİNT', '/foo/bar'))
