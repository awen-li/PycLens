# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: CodePageTest_test_cp1252

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_encode(1252, (('abc', 'strict', b'abc'), ('é€', 'strict', b'\xe9\x80'), ('ÿ', 'strict', b'\xff'), ('Ł', 'strict', None), ('Ł', 'ignore', b''), ('Ł', 'replace', b'L'), ('\udc98', 'surrogateescape', b'\x98'), ('\udc98', 'surrogatepass', None)))
    self.check_decode(1252, ((b'abc', 'strict', 'abc'), (b'\xe9\x80', 'strict', 'é€'), (b'\xff', 'strict', 'ÿ')))
