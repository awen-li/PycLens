# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line_script.py
# case: CmdLineTest_test_hint_when_triying_to_import_a_py_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with os_helper.temp_dir() as script_dir, os_helper.change_cwd(path=script_dir):
        with open('asyncio.py', 'wb'):
            pass
        err = self.check_dash_m_failure('asyncio.py')
        self.assertIn(b"Try using 'asyncio' instead of 'asyncio.py' as the module name", err)
