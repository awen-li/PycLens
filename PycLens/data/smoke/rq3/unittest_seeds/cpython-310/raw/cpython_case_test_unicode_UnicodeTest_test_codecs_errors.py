# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_codecs_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(UnicodeError, 'Andr\x82 x'.encode, 'ascii')
    self.assertRaises(UnicodeError, 'Andr\x82 x'.encode, 'ascii', 'strict')
    self.assertEqual('Andr\x82 x'.encode('ascii', 'ignore'), b'Andr x')
    self.assertEqual('Andr\x82 x'.encode('ascii', 'replace'), b'Andr? x')
    self.assertEqual('Andr\x82 x'.encode('ascii', 'replace'), 'Andr\x82 x'.encode('ascii', errors='replace'))
    self.assertEqual('Andr\x82 x'.encode('ascii', 'ignore'), 'Andr\x82 x'.encode(encoding='ascii', errors='ignore'))
    self.assertRaises(UnicodeError, str, b'Andr\x82 x', 'ascii')
    self.assertRaises(UnicodeError, str, b'Andr\x82 x', 'ascii', 'strict')
    self.assertEqual(str(b'Andr\x82 x', 'ascii', 'ignore'), 'Andr x')
    self.assertEqual(str(b'Andr\x82 x', 'ascii', 'replace'), 'Andr� x')
    self.assertEqual(str(b'\x82 x', 'ascii', 'replace'), '� x')
    self.assertEqual(b'\\N{foo}xx'.decode('unicode-escape', 'ignore'), 'xx')
    self.assertRaises(UnicodeError, b'\\'.decode, 'unicode-escape')
    self.assertRaises(TypeError, b'hello'.decode, 'test.unicode1')
    self.assertRaises(TypeError, str, b'hello', 'test.unicode2')
    self.assertRaises(TypeError, 'hello'.encode, 'test.unicode1')
    self.assertRaises(TypeError, 'hello'.encode, 'test.unicode2')
    self.assertRaises(TypeError, 'hello'.encode, 42, 42, 42)
    self.assertRaises(ValueError, int, '\ud800')
    self.assertRaises(ValueError, int, '\udf00')
    self.assertRaises(ValueError, float, '\ud800')
    self.assertRaises(ValueError, float, '\udf00')
    self.assertRaises(ValueError, complex, '\ud800')
    self.assertRaises(ValueError, complex, '\udf00')
