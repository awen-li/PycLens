# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_codecs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual('hello'.encode('ascii'), b'hello')
    self.assertEqual('hello'.encode('utf-7'), b'hello')
    self.assertEqual('hello'.encode('utf-8'), b'hello')
    self.assertEqual('hello'.encode('utf-8'), b'hello')
    self.assertEqual('hello'.encode('utf-16-le'), b'h\x00e\x00l\x00l\x00o\x00')
    self.assertEqual('hello'.encode('utf-16-be'), b'\x00h\x00e\x00l\x00l\x00o')
    self.assertEqual('hello'.encode('latin-1'), b'hello')
    self.assertEqual('☃'.encode(), b'\xe2\x98\x83')
    for c in range(1024):
        u = chr(c)
        for encoding in ('utf-7', 'utf-8', 'utf-16', 'utf-16-le', 'utf-16-be', 'raw_unicode_escape', 'unicode_escape'):
            self.assertEqual(str(u.encode(encoding), encoding), u)
    for c in range(256):
        u = chr(c)
        for encoding in ('latin-1',):
            self.assertEqual(str(u.encode(encoding), encoding), u)
    for c in range(128):
        u = chr(c)
        for encoding in ('ascii',):
            self.assertEqual(str(u.encode(encoding), encoding), u)
    with warnings.catch_warnings():
        u = '𐀁𠀂𰀃\U00040004\U00050005'
        for encoding in ('utf-8', 'utf-16', 'utf-16-le', 'utf-16-be', 'raw_unicode_escape', 'unicode_escape'):
            self.assertEqual(str(u.encode(encoding), encoding), u)
    u = ''.join(map(chr, list(range(0, 55296)) + list(range(57344, 1114112))))
    for encoding in ('utf-8',):
        self.assertEqual(str(u.encode(encoding), encoding), u)
