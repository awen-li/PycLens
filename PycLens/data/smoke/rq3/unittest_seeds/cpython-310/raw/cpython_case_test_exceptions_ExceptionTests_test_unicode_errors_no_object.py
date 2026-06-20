# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: ExceptionTests_test_unicode_errors_no_object

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    klasses = (UnicodeEncodeError, UnicodeDecodeError, UnicodeTranslateError)
    for klass in klasses:
        self.assertEqual(str(klass.__new__(klass)), '')
