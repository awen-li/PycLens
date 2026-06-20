# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_multiprocessing_main_handling.py
# case: MultiProcessingCmdLineMixin_test_script_compiled

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with os_helper.temp_dir() as script_dir:
        script_name = _make_test_script(script_dir, 'script')
        py_compile.compile(script_name, doraise=True)
        os.remove(script_name)
        pyc_file = import_helper.make_legacy_pyc(script_name)
        self._check_script(pyc_file)
