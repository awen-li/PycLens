# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_struct.py
# case: StructTest_test_unpack_from

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    test_string = b'abcd01234'
    fmt = '4s'
    s = struct.Struct(fmt)
    for cls in (bytes, bytearray):
        data = cls(test_string)
        self.assertEqual(s.unpack_from(data), (b'abcd',))
        self.assertEqual(s.unpack_from(data, 2), (b'cd01',))
        self.assertEqual(s.unpack_from(data, 4), (b'0123',))
        for i in range(6):
            self.assertEqual(s.unpack_from(data, i), (data[i:i + 4],))
        for i in range(6, len(test_string) + 1):
            self.assertRaises(struct.error, s.unpack_from, data, i)
    for cls in (bytes, bytearray):
        data = cls(test_string)
        self.assertEqual(struct.unpack_from(fmt, data), (b'abcd',))
        self.assertEqual(struct.unpack_from(fmt, data, 2), (b'cd01',))
        self.assertEqual(struct.unpack_from(fmt, data, 4), (b'0123',))
        for i in range(6):
            self.assertEqual(struct.unpack_from(fmt, data, i), (data[i:i + 4],))
        for i in range(6, len(test_string) + 1):
            self.assertRaises(struct.error, struct.unpack_from, fmt, data, i)
    self.assertEqual(s.unpack_from(buffer=test_string, offset=2), (b'cd01',))
