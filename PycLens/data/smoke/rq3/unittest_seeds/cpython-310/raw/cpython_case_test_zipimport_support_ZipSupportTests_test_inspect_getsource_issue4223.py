# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipimport_support.py
# case: ZipSupportTests_test_inspect_getsource_issue4223

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    test_src = 'def foo(): pass\n'
    with os_helper.temp_dir() as d:
        init_name = make_script(d, '__init__', test_src)
        name_in_zip = os.path.join('zip_pkg', os.path.basename(init_name))
        (zip_name, run_name) = make_zip_script(d, 'test_zip', init_name, name_in_zip)
        os.remove(init_name)
        sys.path.insert(0, zip_name)
        import zip_pkg
        try:
            self.assertEqual(inspect.getsource(zip_pkg.foo), test_src)
        finally:
            del sys.modules['zip_pkg']
