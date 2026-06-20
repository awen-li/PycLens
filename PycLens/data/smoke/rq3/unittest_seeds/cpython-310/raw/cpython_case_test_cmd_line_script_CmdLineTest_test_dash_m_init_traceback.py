# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line_script.py
# case: CmdLineTest_test_dash_m_init_traceback

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    exceptions = (ImportError, AttributeError, TypeError, ValueError)
    for exception in exceptions:
        exception = exception.__name__
        init = "raise {0}('Exception in __init__.py')".format(exception)
        with self.subTest(exception), self.setup_test_pkg(init) as pkg_dir:
            err = self.check_dash_m_failure('test_pkg')
            self.assertIn(exception.encode('ascii'), err)
            self.assertIn(b'Exception in __init__.py', err)
            self.assertIn(b'Traceback', err)
