# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_isspace_invariant

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for codepoint in range(sys.maxunicode + 1):
        char = chr(codepoint)
        bidirectional = unicodedata.bidirectional(char)
        category = unicodedata.category(char)
        self.assertEqual(char.isspace(), bidirectional in ('WS', 'B', 'S') or category == 'Zs')
