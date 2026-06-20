# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: ImportErrorTests_test_non_str_argument

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with check_warnings(('', BytesWarning), quiet=True):
        arg = b'abc'
        exc = ImportError(arg)
        self.assertEqual(str(arg), str(exc))
