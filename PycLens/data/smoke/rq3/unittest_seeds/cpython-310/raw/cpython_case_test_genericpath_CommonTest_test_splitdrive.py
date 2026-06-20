# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericpath.py
# case: CommonTest_test_splitdrive

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    splitdrive = self.pathmodule.splitdrive
    self.assertEqual(splitdrive('/foo/bar'), ('', '/foo/bar'))
    self.assertEqual(splitdrive('foo:bar'), ('', 'foo:bar'))
    self.assertEqual(splitdrive(':foo:bar'), ('', ':foo:bar'))
    self.assertEqual(splitdrive(b'/foo/bar'), (b'', b'/foo/bar'))
    self.assertEqual(splitdrive(b'foo:bar'), (b'', b'foo:bar'))
    self.assertEqual(splitdrive(b':foo:bar'), (b'', b':foo:bar'))
