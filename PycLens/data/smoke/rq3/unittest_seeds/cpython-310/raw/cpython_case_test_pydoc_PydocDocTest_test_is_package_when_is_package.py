# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: PydocDocTest_test_is_package_when_is_package

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with os_helper.temp_cwd() as test_dir:
        init_path = os.path.join(test_dir, '__init__.py')
        open(init_path, 'w').close()
        self.assertTrue(pydoc.ispackage(test_dir))
        os.remove(init_path)
