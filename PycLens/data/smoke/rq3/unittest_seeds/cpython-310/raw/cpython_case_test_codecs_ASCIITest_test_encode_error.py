# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: ASCIITest_test_encode_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (data, error_handler, expected) in (('[\x80ÿ€]', 'ignore', b'[]'), ('[\x80ÿ€]', 'replace', b'[???]'), ('[\x80ÿ€]', 'xmlcharrefreplace', b'[&#128;&#255;&#8364;]'), ('[\x80ÿ€\U000abcde]', 'backslashreplace', b'[\\x80\\xff\\u20ac\\U000abcde]'), ('[\udc80\udcff]', 'surrogateescape', b'[\x80\xff]')):
        with self.subTest(data=data, error_handler=error_handler, expected=expected):
            self.assertEqual(data.encode('ascii', error_handler), expected)
