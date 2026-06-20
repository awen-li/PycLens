# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_struct.py
# case: StructTest_test_integers_IntTester_test_one

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    format = self.format
    if self.min_value <= x <= self.max_value:
        expected = x
        if self.signed and x < 0:
            expected += 1 << self.bitsize
        self.assertGreaterEqual(expected, 0)
        expected = '%x' % expected
        if len(expected) & 1:
            expected = '0' + expected
        expected = expected.encode('ascii')
        expected = unhexlify(expected)
        expected = b'\x00' * (self.bytesize - len(expected)) + expected
        if self.byteorder == '<' or (self.byteorder in ('', '@', '=') and (not ISBIGENDIAN)):
            expected = string_reverse(expected)
        self.assertEqual(len(expected), self.bytesize)
        got = pack(format, x)
        self.assertEqual(got, expected)
        retrieved = unpack(format, got)[0]
        self.assertEqual(x, retrieved)
        self.assertRaises((struct.error, TypeError), unpack, format, b'\x01' + got)
    else:
        self.assertRaises((OverflowError, ValueError, struct.error), pack, format, x)
