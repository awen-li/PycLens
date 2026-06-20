# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posixpath.py
# case: PosixPathTest_test_join

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(posixpath.join('/foo', 'bar', '/bar', 'baz'), '/bar/baz')
    self.assertEqual(posixpath.join('/foo', 'bar', 'baz'), '/foo/bar/baz')
    self.assertEqual(posixpath.join('/foo/', 'bar/', 'baz/'), '/foo/bar/baz/')
    self.assertEqual(posixpath.join(b'/foo', b'bar', b'/bar', b'baz'), b'/bar/baz')
    self.assertEqual(posixpath.join(b'/foo', b'bar', b'baz'), b'/foo/bar/baz')
    self.assertEqual(posixpath.join(b'/foo/', b'bar/', b'baz/'), b'/foo/bar/baz/')
