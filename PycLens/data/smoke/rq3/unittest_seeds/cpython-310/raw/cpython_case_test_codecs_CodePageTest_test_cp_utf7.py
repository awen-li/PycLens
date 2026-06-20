# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: CodePageTest_test_cp_utf7

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cp = 65000
    self.check_encode(cp, (('abc', 'strict', b'abc'), ('é€', 'strict', b'+AOkgrA-'), ('\U0010ffff', 'strict', b'+2//f/w-'), ('\udc80', 'strict', b'+3IA-'), ('�', 'strict', b'+//0-')))
    self.check_decode(cp, ((b'abc', 'strict', 'abc'), (b'+AOkgrA-', 'strict', 'é€'), (b'+2//f/w-', 'strict', '\U0010ffff'), (b'+3IA-', 'strict', '\udc80'), (b'+//0-', 'strict', '�'), (b'[+/]', 'strict', '[]'), (b'[\xff]', 'strict', '[ÿ]')))
