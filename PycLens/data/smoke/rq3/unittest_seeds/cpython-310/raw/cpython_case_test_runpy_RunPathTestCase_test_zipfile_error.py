# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_runpy.py
# case: RunPathTestCase_test_zipfile_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with temp_dir() as script_dir:
        mod_name = 'not_main'
        script_name = self._make_test_script(script_dir, mod_name)
        (zip_name, fname) = make_zip_script(script_dir, 'test_zip', script_name)
        msg = "can't find '__main__' module in %r" % zip_name
        self._check_import_error(zip_name, msg)
