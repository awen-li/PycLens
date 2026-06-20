# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exception_hierarchy.py
# case: AttributesTest_test_posix_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    e = OSError(EEXIST, 'File already exists', 'foo.txt')
    self.assertEqual(e.errno, EEXIST)
    self.assertEqual(e.args[0], EEXIST)
    self.assertEqual(e.strerror, 'File already exists')
    self.assertEqual(e.filename, 'foo.txt')
    if os.name == 'nt':
        self.assertEqual(e.winerror, None)
