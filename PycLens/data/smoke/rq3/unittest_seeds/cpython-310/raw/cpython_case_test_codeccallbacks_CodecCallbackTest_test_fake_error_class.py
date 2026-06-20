# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codeccallbacks.py
# case: CodecCallbackTest_test_fake_error_class

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    handlers = [codecs.strict_errors, codecs.ignore_errors, codecs.replace_errors, codecs.backslashreplace_errors, codecs.namereplace_errors, codecs.xmlcharrefreplace_errors, codecs.lookup_error('surrogateescape'), codecs.lookup_error('surrogatepass')]
    for cls in (UnicodeEncodeError, UnicodeDecodeError, UnicodeTranslateError):

        class FakeUnicodeError(str):
            __class__ = cls
        for handler in handlers:
            with self.subTest(handler=handler, error_class=cls):
                self.assertRaises(TypeError, handler, FakeUnicodeError())

        class FakeUnicodeError(Exception):
            __class__ = cls
        for handler in handlers:
            with self.subTest(handler=handler, error_class=cls):
                with self.assertRaises((TypeError, FakeUnicodeError)):
                    handler(FakeUnicodeError())
