# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestTemporaryDirectory_test_explicit_cleanup

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dir = tempfile.mkdtemp()
    try:
        d = self.do_create(dir=dir)
        self.assertTrue(os.path.exists(d.name), 'TemporaryDirectory %s does not exist' % d.name)
        d.cleanup()
        self.assertFalse(os.path.exists(d.name), 'TemporaryDirectory %s exists after cleanup' % d.name)
    finally:
        os.rmdir(dir)
