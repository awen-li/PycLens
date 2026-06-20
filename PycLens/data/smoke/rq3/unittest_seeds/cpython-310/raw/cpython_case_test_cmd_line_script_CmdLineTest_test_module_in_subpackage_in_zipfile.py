# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line_script.py
# case: CmdLineTest_test_module_in_subpackage_in_zipfile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with os_helper.temp_dir() as script_dir:
        (zip_name, run_name) = _make_test_zip_pkg(script_dir, 'test_zip', 'test_pkg', 'script', depth=2)
        self._check_script(['-m', 'test_pkg.test_pkg.script'], run_name, run_name, script_dir, 'test_pkg.test_pkg', zipimport.zipimporter, PYTHONPATH=zip_name, cwd=script_dir)
