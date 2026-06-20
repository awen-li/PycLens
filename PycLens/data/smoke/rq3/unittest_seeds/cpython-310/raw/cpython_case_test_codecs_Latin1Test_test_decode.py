# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: Latin1Test_test_decode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (data, expected) in ((b'abc', 'abc'), (b'[\x80\xff]', '[\x80ÿ]')):
        with self.subTest(data=data, expected=expected):
            self.assertEqual(data.decode('latin1'), expected)
