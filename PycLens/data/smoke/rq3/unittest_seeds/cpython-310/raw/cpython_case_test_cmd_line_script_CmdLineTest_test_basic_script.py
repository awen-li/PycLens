# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line_script.py
# case: CmdLineTest_test_basic_script

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with os_helper.temp_dir() as script_dir:
        script_name = _make_test_script(script_dir, 'script')
        self._check_script(script_name, script_name, script_name, script_dir, None, importlib.machinery.SourceFileLoader, expected_cwd=script_dir)
