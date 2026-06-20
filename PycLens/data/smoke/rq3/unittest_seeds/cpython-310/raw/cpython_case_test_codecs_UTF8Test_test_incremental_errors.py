# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: UTF8Test_test_incremental_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cases = [b'\x80', b'\xbf', b'\xc0', b'\xc1', b'\xf5', b'\xf6', b'\xff']
    for prefix in (b'\xc2', b'\xdf', b'\xe0', b'\xe0\xa0', b'\xef', b'\xef\xbf', b'\xf0', b'\xf0\x90', b'\xf0\x90\x80', b'\xf4', b'\xf4\x8f', b'\xf4\x8f\xbf'):
        for suffix in (b'\x7f', b'\xc0'):
            cases.append(prefix + suffix)
    cases.extend((b'\xe0\x80', b'\xe0\x9f', b'\xed\xa0\x80', b'\xed\xbf\xbf', b'\xf0\x80', b'\xf0\x8f', b'\xf4\x90'))
    for data in cases:
        with self.subTest(data=data):
            dec = codecs.getincrementaldecoder(self.encoding)()
            self.assertRaises(UnicodeDecodeError, dec.decode, data)
