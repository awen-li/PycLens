# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posixpath.py
# case: PosixPathTest_test_relpath

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (real_getcwd, os.getcwd) = (os.getcwd, lambda : '/home/user/bar')
    try:
        curdir = os.path.split(os.getcwd())[-1]
        self.assertRaises(ValueError, posixpath.relpath, '')
        self.assertEqual(posixpath.relpath('a'), 'a')
        self.assertEqual(posixpath.relpath(posixpath.abspath('a')), 'a')
        self.assertEqual(posixpath.relpath('a/b'), 'a/b')
        self.assertEqual(posixpath.relpath('../a/b'), '../a/b')
        self.assertEqual(posixpath.relpath('a', '../b'), '../' + curdir + '/a')
        self.assertEqual(posixpath.relpath('a/b', '../c'), '../' + curdir + '/a/b')
        self.assertEqual(posixpath.relpath('a', 'b/c'), '../../a')
        self.assertEqual(posixpath.relpath('a', 'a'), '.')
        self.assertEqual(posixpath.relpath('/foo/bar/bat', '/x/y/z'), '../../../foo/bar/bat')
        self.assertEqual(posixpath.relpath('/foo/bar/bat', '/foo/bar'), 'bat')
        self.assertEqual(posixpath.relpath('/foo/bar/bat', '/'), 'foo/bar/bat')
        self.assertEqual(posixpath.relpath('/', '/foo/bar/bat'), '../../..')
        self.assertEqual(posixpath.relpath('/foo/bar/bat', '/x'), '../foo/bar/bat')
        self.assertEqual(posixpath.relpath('/x', '/foo/bar/bat'), '../../../x')
        self.assertEqual(posixpath.relpath('/', '/'), '.')
        self.assertEqual(posixpath.relpath('/a', '/a'), '.')
        self.assertEqual(posixpath.relpath('/a/b', '/a/b'), '.')
    finally:
        os.getcwd = real_getcwd
