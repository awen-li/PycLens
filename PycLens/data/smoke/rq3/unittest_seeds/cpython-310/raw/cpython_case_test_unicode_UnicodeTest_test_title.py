# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_title

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    super().test_title()
    self.assertEqual('𐑏'.title(), '𐐧')
    self.assertEqual('𐑏𐑏'.title(), '𐐧𐑏')
    self.assertEqual('𐑏𐑏 𐑏𐑏'.title(), '𐐧𐑏 𐐧𐑏')
    self.assertEqual('𐐧𐑏 𐐧𐑏'.title(), '𐐧𐑏 𐐧𐑏')
    self.assertEqual('𐑏𐐧 𐑏𐐧'.title(), '𐐧𐑏 𐐧𐑏')
    self.assertEqual('X𐐧x𐑏 X𐐧x𐑏'.title(), 'X𐑏x𐑏 X𐑏x𐑏')
    self.assertEqual('ﬁNNISH'.title(), 'Finnish')
    self.assertEqual('AΣ ᾡxy'.title(), 'Aς ᾩxy')
    self.assertEqual('AΣA'.title(), 'Aσa')
