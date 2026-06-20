# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: CodePageTest_test_multibyte_encoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_decode(932, ((b'\x84\xe9\x80', 'ignore', '騾'), (b'\x84\xe9\x80', 'replace', '�騾')))
    self.check_decode(self.CP_UTF8, ((b'\xff\xf4\x8f\xbf\xbf', 'ignore', '\U0010ffff'), (b'\xff\xf4\x8f\xbf\xbf', 'replace', '�\U0010ffff')))
    self.check_encode(self.CP_UTF8, (('[\U0010ffff\udc80]', 'ignore', b'[\xf4\x8f\xbf\xbf]'), ('[\U0010ffff\udc80]', 'replace', b'[\xf4\x8f\xbf\xbf?]')))
