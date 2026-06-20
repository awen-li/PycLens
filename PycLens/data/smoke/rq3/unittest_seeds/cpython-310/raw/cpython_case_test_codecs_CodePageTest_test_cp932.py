# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: CodePageTest_test_cp932

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_encode(932, (('abc', 'strict', b'abc'), ('ｄ騾', 'strict', b'\x82\x84\xe9\x80'), ('ÿ', 'strict', None), ('[ÿ]', 'ignore', b'[]'), ('[ÿ]', 'replace', b'[y]'), ('[€]', 'replace', b'[?]'), ('[ÿ]', 'backslashreplace', b'[\\xff]'), ('[ÿ]', 'namereplace', b'[\\N{LATIN SMALL LETTER Y WITH DIAERESIS}]'), ('[ÿ]', 'xmlcharrefreplace', b'[&#255;]'), ('\udcff', 'strict', None), ('[\udcff]', 'surrogateescape', b'[\xff]'), ('[\udcff]', 'surrogatepass', None)))
    self.check_decode(932, ((b'abc', 'strict', 'abc'), (b'\x82\x84\xe9\x80', 'strict', 'ｄ騾'), (b'[\xff]', 'strict', None), (b'[\xff]', 'ignore', '[]'), (b'[\xff]', 'replace', '[�]'), (b'[\xff]', 'backslashreplace', '[\\xff]'), (b'[\xff]', 'surrogateescape', '[\udcff]'), (b'[\xff]', 'surrogatepass', None), (b'\x81\x00abc', 'strict', None), (b'\x81\x00abc', 'ignore', '\x00abc'), (b'\x81\x00abc', 'replace', '�\x00abc'), (b'\x81\x00abc', 'backslashreplace', '\\x81\x00abc')))
