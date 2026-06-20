# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: UnicodeEscapeTest_test_partial

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_partial('\x00\t\n\r\\ÿ\uffff𐀀', ['', '', '', '\x00', '\x00', '\x00\t', '\x00\t', '\x00\t\n', '\x00\t\n', '\x00\t\n\r', '\x00\t\n\r', '\x00\t\n\r\\', '\x00\t\n\r\\', '\x00\t\n\r\\', '\x00\t\n\r\\', '\x00\t\n\r\\ÿ', '\x00\t\n\r\\ÿ', '\x00\t\n\r\\ÿ', '\x00\t\n\r\\ÿ', '\x00\t\n\r\\ÿ', '\x00\t\n\r\\ÿ', '\x00\t\n\r\\ÿ\uffff', '\x00\t\n\r\\ÿ\uffff', '\x00\t\n\r\\ÿ\uffff', '\x00\t\n\r\\ÿ\uffff', '\x00\t\n\r\\ÿ\uffff', '\x00\t\n\r\\ÿ\uffff', '\x00\t\n\r\\ÿ\uffff', '\x00\t\n\r\\ÿ\uffff', '\x00\t\n\r\\ÿ\uffff', '\x00\t\n\r\\ÿ\uffff', '\x00\t\n\r\\ÿ\uffff𐀀'])
