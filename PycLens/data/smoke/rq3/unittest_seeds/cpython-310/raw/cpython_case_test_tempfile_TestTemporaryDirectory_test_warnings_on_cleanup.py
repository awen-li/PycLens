# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestTemporaryDirectory_test_warnings_on_cleanup

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.do_create() as dir:
        d = self.do_create(dir=dir, recurse=3)
        name = d.name
        with warnings_helper.check_warnings(('Implicitly', ResourceWarning), quiet=False):
            warnings.filterwarnings('always', category=ResourceWarning)
            del d
            support.gc_collect()
        self.assertFalse(os.path.exists(name), 'TemporaryDirectory %s exists after __del__' % name)
