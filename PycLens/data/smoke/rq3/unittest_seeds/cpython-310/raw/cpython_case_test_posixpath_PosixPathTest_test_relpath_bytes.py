# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posixpath.py
# case: PosixPathTest_test_relpath_bytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (real_getcwdb, os.getcwdb) = (os.getcwdb, lambda : b'/home/user/bar')
    try:
        curdir = os.path.split(os.getcwdb())[-1]
        self.assertRaises(ValueError, posixpath.relpath, b'')
        self.assertEqual(posixpath.relpath(b'a'), b'a')
        self.assertEqual(posixpath.relpath(posixpath.abspath(b'a')), b'a')
        self.assertEqual(posixpath.relpath(b'a/b'), b'a/b')
        self.assertEqual(posixpath.relpath(b'../a/b'), b'../a/b')
        self.assertEqual(posixpath.relpath(b'a', b'../b'), b'../' + curdir + b'/a')
        self.assertEqual(posixpath.relpath(b'a/b', b'../c'), b'../' + curdir + b'/a/b')
        self.assertEqual(posixpath.relpath(b'a', b'b/c'), b'../../a')
        self.assertEqual(posixpath.relpath(b'a', b'a'), b'.')
        self.assertEqual(posixpath.relpath(b'/foo/bar/bat', b'/x/y/z'), b'../../../foo/bar/bat')
        self.assertEqual(posixpath.relpath(b'/foo/bar/bat', b'/foo/bar'), b'bat')
        self.assertEqual(posixpath.relpath(b'/foo/bar/bat', b'/'), b'foo/bar/bat')
        self.assertEqual(posixpath.relpath(b'/', b'/foo/bar/bat'), b'../../..')
        self.assertEqual(posixpath.relpath(b'/foo/bar/bat', b'/x'), b'../foo/bar/bat')
        self.assertEqual(posixpath.relpath(b'/x', b'/foo/bar/bat'), b'../../../x')
        self.assertEqual(posixpath.relpath(b'/', b'/'), b'.')
        self.assertEqual(posixpath.relpath(b'/a', b'/a'), b'.')
        self.assertEqual(posixpath.relpath(b'/a/b', b'/a/b'), b'.')
        self.assertRaises(TypeError, posixpath.relpath, b'bytes', 'str')
        self.assertRaises(TypeError, posixpath.relpath, 'str', b'bytes')
    finally:
        os.getcwdb = real_getcwdb
