# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_runpy.py
# case: RunPathTestCase_test_directory_compiled

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with temp_dir() as script_dir:
        mod_name = '__main__'
        script_name = self._make_test_script(script_dir, mod_name)
        compiled_name = py_compile.compile(script_name, doraise=True)
        os.remove(script_name)
        if not sys.dont_write_bytecode:
            legacy_pyc = make_legacy_pyc(script_name)
            self._check_script(script_dir, '<run_path>', legacy_pyc, script_dir, mod_name=mod_name)
