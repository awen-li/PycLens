# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: Latin1Test_test_encode_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (data, error_handler, expected) in (('[€\udc80]', 'ignore', b'[]'), ('[€\udc80]', 'replace', b'[??]'), ('[€\U000abcde]', 'backslashreplace', b'[\\u20ac\\U000abcde]'), ('[€\udc80]', 'xmlcharrefreplace', b'[&#8364;&#56448;]'), ('[\udc80\udcff]', 'surrogateescape', b'[\x80\xff]')):
        with self.subTest(data=data, error_handler=error_handler, expected=expected):
            self.assertEqual(data.encode('latin1', error_handler), expected)
