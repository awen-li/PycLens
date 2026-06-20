# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_conversion

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class ObjectToStr:

        def __str__(self):
            return 'foo'

    class StrSubclassToStr(str):

        def __str__(self):
            return 'foo'

    class StrSubclassToStrSubclass(str):

        def __new__(cls, content=''):
            return str.__new__(cls, 2 * content)

        def __str__(self):
            return self
    self.assertEqual(str(ObjectToStr()), 'foo')
    self.assertEqual(str(StrSubclassToStr('bar')), 'foo')
    s = str(StrSubclassToStrSubclass('foo'))
    self.assertEqual(s, 'foofoo')
    self.assertIs(type(s), StrSubclassToStrSubclass)
    s = StrSubclass(StrSubclassToStrSubclass('foo'))
    self.assertEqual(s, 'foofoo')
    self.assertIs(type(s), StrSubclass)
