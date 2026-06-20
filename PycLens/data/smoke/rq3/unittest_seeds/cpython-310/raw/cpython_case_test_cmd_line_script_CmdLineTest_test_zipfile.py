# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line_script.py
# case: CmdLineTest_test_zipfile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with os_helper.temp_dir() as script_dir:
        script_name = _make_test_script(script_dir, '__main__')
        (zip_name, run_name) = make_zip_script(script_dir, 'test_zip', script_name)
        self._check_script(zip_name, run_name, zip_name, zip_name, '', zipimport.zipimporter)
