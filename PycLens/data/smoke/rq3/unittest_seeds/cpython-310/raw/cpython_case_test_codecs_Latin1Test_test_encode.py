# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: Latin1Test_test_encode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (data, expected) in (('abc', b'abc'), ('\x80éÿ', b'\x80\xe9\xff')):
        with self.subTest(data=data, expected=expected):
            self.assertEqual(data.encode('latin1'), expected)
