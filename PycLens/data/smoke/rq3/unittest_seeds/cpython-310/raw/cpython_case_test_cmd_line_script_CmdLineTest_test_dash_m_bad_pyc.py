# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line_script.py
# case: CmdLineTest_test_dash_m_bad_pyc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with os_helper.temp_dir() as script_dir, os_helper.change_cwd(path=script_dir):
        os.mkdir('test_pkg')
        with open('test_pkg/__init__.pyc', 'wb'):
            pass
        err = self.check_dash_m_failure('test_pkg')
        self.assertRegex(err, b'Error while finding module specification.*ImportError.*bad magic number')
        self.assertNotIn(b'is a package', err)
        self.assertNotIn(b'Traceback', err)
