# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imp.py
# case: ImportTests_test_find_and_load_checked_pyc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with os_helper.temp_cwd():
        with open('mymod.py', 'wb') as fp:
            fp.write(b'x = 42\n')
        py_compile.compile('mymod.py', doraise=True, invalidation_mode=py_compile.PycInvalidationMode.CHECKED_HASH)
        (file, path, description) = imp.find_module('mymod', path=['.'])
        mod = imp.load_module('mymod', file, path, description)
    self.assertEqual(mod.x, 42)
