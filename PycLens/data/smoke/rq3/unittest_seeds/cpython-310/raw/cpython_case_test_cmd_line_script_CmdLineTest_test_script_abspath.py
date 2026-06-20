# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line_script.py
# case: CmdLineTest_test_script_abspath

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with os_helper.temp_cwd() as script_dir:
        self.assertTrue(os.path.isabs(script_dir), script_dir)
        script_name = _make_test_script(script_dir, 'script')
        relative_name = os.path.basename(script_name)
        self._check_script(relative_name, script_name, relative_name, script_dir, None, importlib.machinery.SourceFileLoader)
