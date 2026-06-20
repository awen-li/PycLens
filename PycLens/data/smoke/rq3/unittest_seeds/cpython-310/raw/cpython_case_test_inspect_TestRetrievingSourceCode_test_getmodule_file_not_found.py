# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestRetrievingSourceCode_test_getmodule_file_not_found

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def _getabsfile(obj, _filename):
        raise FileNotFoundError('bad file')
    with unittest.mock.patch('inspect.getabsfile', _getabsfile):
        f = inspect.currentframe()
        self.assertIsNone(inspect.getmodule(f))
        inspect.getouterframes(f)
