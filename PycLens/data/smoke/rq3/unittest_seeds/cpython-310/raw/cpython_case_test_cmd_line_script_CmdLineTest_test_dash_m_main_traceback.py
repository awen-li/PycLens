# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line_script.py
# case: CmdLineTest_test_dash_m_main_traceback

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.setup_test_pkg() as pkg_dir:
        main = "raise ImportError('Exception in __main__ module')"
        _make_test_script(pkg_dir, '__main__', main)
        err = self.check_dash_m_failure('test_pkg')
        self.assertIn(b'ImportError', err)
        self.assertIn(b'Exception in __main__ module', err)
        self.assertIn(b'Traceback', err)
