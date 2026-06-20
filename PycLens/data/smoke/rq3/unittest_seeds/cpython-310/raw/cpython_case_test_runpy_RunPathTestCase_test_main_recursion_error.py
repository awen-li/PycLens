# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_runpy.py
# case: RunPathTestCase_test_main_recursion_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with temp_dir() as script_dir, temp_dir() as dummy_dir:
        mod_name = '__main__'
        source = 'import runpy\nrunpy.run_path(%r)\n' % dummy_dir
        script_name = self._make_test_script(script_dir, mod_name, source)
        (zip_name, fname) = make_zip_script(script_dir, 'test_zip', script_name)
        self.assertRaises(RecursionError, run_path, zip_name)
