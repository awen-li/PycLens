# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_constructor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(str('unicode remains unicode'), 'unicode remains unicode')
    for text in ('ascii', 'é', '€', '\U0010ffff'):
        subclass = StrSubclass(text)
        self.assertEqual(str(subclass), text)
        self.assertEqual(len(subclass), len(text))
        if text == 'ascii':
            self.assertEqual(subclass.encode('ascii'), b'ascii')
            self.assertEqual(subclass.encode('utf-8'), b'ascii')
    self.assertEqual(str('strings are converted to unicode'), 'strings are converted to unicode')

    class StringCompat:

        def __init__(self, x):
            self.x = x

        def __str__(self):
            return self.x
    self.assertEqual(str(StringCompat('__str__ compatible objects are recognized')), '__str__ compatible objects are recognized')
    o = StringCompat('unicode(obj) is compatible to str()')
    self.assertEqual(str(o), 'unicode(obj) is compatible to str()')
    self.assertEqual(str(o), 'unicode(obj) is compatible to str()')
    for obj in (123, 123.45, 123):
        self.assertEqual(str(obj), str(str(obj)))
    if not sys.platform.startswith('java'):
        self.assertRaises(TypeError, str, 'decoding unicode is not supported', 'utf-8', 'strict')
    self.assertEqual(str(b'strings are decoded to unicode', 'utf-8', 'strict'), 'strings are decoded to unicode')
    if not sys.platform.startswith('java'):
        self.assertEqual(str(memoryview(b'character buffers are decoded to unicode'), 'utf-8', 'strict'), 'character buffers are decoded to unicode')
    self.assertRaises(TypeError, str, 42, 42, 42)
