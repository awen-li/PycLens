# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: CodecsModuleTest_test_undefined

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(UnicodeError, codecs.encode, 'abc', 'undefined')
    self.assertRaises(UnicodeError, codecs.decode, b'abc', 'undefined')
    self.assertRaises(UnicodeError, codecs.encode, '', 'undefined')
    self.assertRaises(UnicodeError, codecs.decode, b'', 'undefined')
    for errors in ('strict', 'ignore', 'replace', 'backslashreplace'):
        self.assertRaises(UnicodeError, codecs.encode, 'abc', 'undefined', errors)
        self.assertRaises(UnicodeError, codecs.decode, b'abc', 'undefined', errors)
