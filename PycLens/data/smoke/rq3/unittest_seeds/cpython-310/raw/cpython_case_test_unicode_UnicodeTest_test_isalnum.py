# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_isalnum

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    super().test_isalnum()
    for ch in ['𐐁', '𐐧', '𐐩', '𐑎', '𝟶', '𑁦', '𐒠', '🄇']:
        self.assertTrue(ch.isalnum(), '{!a} is alnum.'.format(ch))
