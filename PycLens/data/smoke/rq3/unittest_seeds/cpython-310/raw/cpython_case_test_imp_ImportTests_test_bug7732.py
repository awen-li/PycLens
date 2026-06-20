# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imp.py
# case: ImportTests_test_bug7732

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with os_helper.temp_cwd():
        source = os_helper.TESTFN + '.py'
        os.mkdir(source)
        self.assertRaisesRegex(ImportError, '^No module', imp.find_module, os_helper.TESTFN, ['.'])
