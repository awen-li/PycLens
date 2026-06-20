# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_multiprocessing_main_handling.py
# case: MultiProcessingCmdLineMixin_test_zipfile_compiled

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    source = self.main_in_children_source
    with os_helper.temp_dir() as script_dir:
        script_name = _make_test_script(script_dir, '__main__', source=source)
        compiled_name = py_compile.compile(script_name, doraise=True)
        (zip_name, run_name) = make_zip_script(script_dir, 'test_zip', compiled_name)
        self._check_script(zip_name)
