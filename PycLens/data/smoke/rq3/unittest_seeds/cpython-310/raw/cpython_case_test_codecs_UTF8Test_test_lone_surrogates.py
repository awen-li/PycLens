# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: UTF8Test_test_lone_surrogates

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    super().test_lone_surrogates()
    self.assertEqual('[\udc80]'.encode(self.encoding, 'surrogateescape'), self.BOM + b'[\x80]')
    with self.assertRaises(UnicodeEncodeError) as cm:
        '[\udc80\ud800\udfff]'.encode(self.encoding, 'surrogateescape')
    exc = cm.exception
    self.assertEqual(exc.object[exc.start:exc.end], '\ud800\udfff')
