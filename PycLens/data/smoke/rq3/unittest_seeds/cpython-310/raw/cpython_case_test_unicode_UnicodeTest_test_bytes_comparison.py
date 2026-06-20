# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_bytes_comparison

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with warnings_helper.check_warnings():
        warnings.simplefilter('ignore', BytesWarning)
        self.assertEqual('abc' == b'abc', False)
        self.assertEqual('abc' != b'abc', True)
        self.assertEqual('abc' == bytearray(b'abc'), False)
        self.assertEqual('abc' != bytearray(b'abc'), True)
