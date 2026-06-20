# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: ExceptionTests_test_unicode_change_attributes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    u = UnicodeEncodeError('baz', 'xxxxx', 1, 5, 'foo')
    self.assertEqual(str(u), "'baz' codec can't encode characters in position 1-4: foo")
    u.end = 2
    self.assertEqual(str(u), "'baz' codec can't encode character '\\x78' in position 1: foo")
    u.end = 5
    u.reason = 965230951443685724997
    self.assertEqual(str(u), "'baz' codec can't encode characters in position 1-4: 965230951443685724997")
    u.encoding = 4000
    self.assertEqual(str(u), "'4000' codec can't encode characters in position 1-4: 965230951443685724997")
    u.start = 1000
    self.assertEqual(str(u), "'4000' codec can't encode characters in position 1000-4: 965230951443685724997")
    u = UnicodeDecodeError('baz', b'xxxxx', 1, 5, 'foo')
    self.assertEqual(str(u), "'baz' codec can't decode bytes in position 1-4: foo")
    u.end = 2
    self.assertEqual(str(u), "'baz' codec can't decode byte 0x78 in position 1: foo")
    u.end = 5
    u.reason = 965230951443685724997
    self.assertEqual(str(u), "'baz' codec can't decode bytes in position 1-4: 965230951443685724997")
    u.encoding = 4000
    self.assertEqual(str(u), "'4000' codec can't decode bytes in position 1-4: 965230951443685724997")
    u.start = 1000
    self.assertEqual(str(u), "'4000' codec can't decode bytes in position 1000-4: 965230951443685724997")
    u = UnicodeTranslateError('xxxx', 1, 5, 'foo')
    self.assertEqual(str(u), "can't translate characters in position 1-4: foo")
    u.end = 2
    self.assertEqual(str(u), "can't translate character '\\x78' in position 1: foo")
    u.end = 5
    u.reason = 965230951443685724997
    self.assertEqual(str(u), "can't translate characters in position 1-4: 965230951443685724997")
    u.start = 1000
    self.assertEqual(str(u), "can't translate characters in position 1000-4: 965230951443685724997")
