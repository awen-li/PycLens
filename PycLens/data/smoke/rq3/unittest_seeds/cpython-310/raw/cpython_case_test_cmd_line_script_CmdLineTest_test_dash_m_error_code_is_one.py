# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line_script.py
# case: CmdLineTest_test_dash_m_error_code_is_one

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.setup_test_pkg() as pkg_dir:
        script_name = _make_test_script(pkg_dir, 'other', "if __name__ == '__main__': raise ValueError")
        err = self.check_dash_m_failure('test_pkg.other', *example_args)
        self.assertIn(b'ValueError', err)
