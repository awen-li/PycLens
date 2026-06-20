# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_runpy.py
# case: RunPathTestCase_test_directory

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with temp_dir() as script_dir:
        mod_name = '__main__'
        script_name = self._make_test_script(script_dir, mod_name)
        self._check_script(script_dir, '<run_path>', script_name, script_dir, mod_name=mod_name)
