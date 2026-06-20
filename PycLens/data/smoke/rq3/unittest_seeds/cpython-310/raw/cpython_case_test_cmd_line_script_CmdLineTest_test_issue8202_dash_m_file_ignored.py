# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line_script.py
# case: CmdLineTest_test_issue8202_dash_m_file_ignored

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with os_helper.temp_dir() as script_dir:
        script_name = _make_test_script(script_dir, 'other')
        with os_helper.change_cwd(path=script_dir):
            with open('-m', 'w', encoding='utf-8') as f:
                f.write('data')
                (rc, out, err) = assert_python_ok('-m', 'other', *example_args, __isolated=False)
                self._check_output(script_name, rc, out, script_name, script_name, script_dir, '', importlib.machinery.SourceFileLoader)
