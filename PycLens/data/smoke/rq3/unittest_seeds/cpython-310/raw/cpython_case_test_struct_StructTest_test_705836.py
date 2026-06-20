# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_struct.py
# case: StructTest_test_705836

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for base in range(1, 33):
        delta = 0.5
        while base - delta / 2.0 != base:
            delta /= 2.0
        smaller = base - delta
        packed = struct.pack('<f', smaller)
        unpacked = struct.unpack('<f', packed)[0]
        self.assertEqual(base, unpacked)
        bigpacked = struct.pack('>f', smaller)
        self.assertEqual(bigpacked, string_reverse(packed))
        unpacked = struct.unpack('>f', bigpacked)[0]
        self.assertEqual(base, unpacked)
    big = (1 << 24) - 1
    big = math.ldexp(big, 127 - 23)
    packed = struct.pack('>f', big)
    unpacked = struct.unpack('>f', packed)[0]
    self.assertEqual(big, unpacked)
    big = (1 << 25) - 1
    big = math.ldexp(big, 127 - 24)
    self.assertRaises(OverflowError, struct.pack, '>f', big)
