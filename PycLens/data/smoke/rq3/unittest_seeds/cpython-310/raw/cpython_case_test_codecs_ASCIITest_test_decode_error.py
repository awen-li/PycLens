# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: ASCIITest_test_decode_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (data, error_handler, expected) in ((b'[\x80\xff]', 'ignore', '[]'), (b'[\x80\xff]', 'replace', '[��]'), (b'[\x80\xff]', 'surrogateescape', '[\udc80\udcff]'), (b'[\x80\xff]', 'backslashreplace', '[\\x80\\xff]')):
        with self.subTest(data=data, error_handler=error_handler, expected=expected):
            self.assertEqual(data.decode('ascii', error_handler), expected)
