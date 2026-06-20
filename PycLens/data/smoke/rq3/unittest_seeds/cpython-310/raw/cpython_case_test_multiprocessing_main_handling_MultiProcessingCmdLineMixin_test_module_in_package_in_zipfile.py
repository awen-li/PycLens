# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_multiprocessing_main_handling.py
# case: MultiProcessingCmdLineMixin_test_module_in_package_in_zipfile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with os_helper.temp_dir() as script_dir:
        (zip_name, run_name) = _make_test_zip_pkg(script_dir, 'test_zip', 'test_pkg', 'script')
        launch_name = _make_launch_script(script_dir, 'launch', 'test_pkg.script', zip_name)
        self._check_script(launch_name)
