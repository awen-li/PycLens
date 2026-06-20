# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_exception_bad_args_0

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    desired_exception = self._get_chdir_exception()
    try:
        p = subprocess.Popen([self._nonexistent_dir, '-c', ''])
    except OSError as e:
        self.assertEqual(desired_exception.errno, e.errno)
        self.assertEqual(desired_exception.strerror, e.strerror)
        self.assertEqual(desired_exception.filename, e.filename)
    else:
        self.fail('Expected OSError: %s' % desired_exception)
