# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_struct.py
# case: UnpackIteratorTest_test_half_float

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    format_bits_float__cleanRoundtrip_list = [(b'\x00<', 1.0), (b'\x00\xc0', -2.0), (b'\xff{', 65504.0), (b'\x00\x04', 2 ** (-14)), (b'\x01\x00', 2 ** (-24)), (b'\x00\x00', 0.0), (b'\x00\x80', -0.0), (b'\x00|', float('+inf')), (b'\x00\xfc', float('-inf')), (b'U5', 0.333251953125)]
    for (le_bits, f) in format_bits_float__cleanRoundtrip_list:
        be_bits = le_bits[::-1]
        self.assertEqual(f, struct.unpack('<e', le_bits)[0])
        self.assertEqual(le_bits, struct.pack('<e', f))
        self.assertEqual(f, struct.unpack('>e', be_bits)[0])
        self.assertEqual(be_bits, struct.pack('>e', f))
        if sys.byteorder == 'little':
            self.assertEqual(f, struct.unpack('e', le_bits)[0])
            self.assertEqual(le_bits, struct.pack('e', f))
        else:
            self.assertEqual(f, struct.unpack('e', be_bits)[0])
            self.assertEqual(be_bits, struct.pack('e', f))
    format_bits__nan_list = [('<e', b'\x01\xfc'), ('<e', b'\x00\xfe'), ('<e', b'\xff\xff'), ('<e', b'\x01|'), ('<e', b'\x00~'), ('<e', b'\xff\x7f')]
    for (formatcode, bits) in format_bits__nan_list:
        self.assertTrue(math.isnan(struct.unpack('<e', bits)[0]))
        self.assertTrue(math.isnan(struct.unpack('>e', bits[::-1])[0]))
    packed = struct.pack('<e', math.nan)
    self.assertEqual(packed[1] & 126, 126)
    packed = struct.pack('<e', -math.nan)
    self.assertEqual(packed[1] & 126, 126)
    format_bits_float__rounding_list = [('>e', b'\x00\x01', 2.0 ** (-25) + 2.0 ** (-35)), ('>e', b'\x00\x00', 2.0 ** (-25)), ('>e', b'\x00\x00', 2.0 ** (-26)), ('>e', b'\x03\xff', 2.0 ** (-14) - 2.0 ** (-24)), ('>e', b'\x03\xff', 2.0 ** (-14) - 2.0 ** (-25) - 2.0 ** (-65)), ('>e', b'\x04\x00', 2.0 ** (-14) - 2.0 ** (-25)), ('>e', b'\x04\x00', 2.0 ** (-14)), ('>e', b'<\x01', 1.0 + 2.0 ** (-11) + 2.0 ** (-16)), ('>e', b'<\x00', 1.0 + 2.0 ** (-11)), ('>e', b'<\x00', 1.0 + 2.0 ** (-12)), ('>e', b'{\xff', 65504), ('>e', b'{\xff', 65519), ('>e', b'\x80\x01', -2.0 ** (-25) - 2.0 ** (-35)), ('>e', b'\x80\x00', -2.0 ** (-25)), ('>e', b'\x80\x00', -2.0 ** (-26)), ('>e', b'\xbc\x01', -1.0 - 2.0 ** (-11) - 2.0 ** (-16)), ('>e', b'\xbc\x00', -1.0 - 2.0 ** (-11)), ('>e', b'\xbc\x00', -1.0 - 2.0 ** (-12)), ('>e', b'\xfb\xff', -65519)]
    for (formatcode, bits, f) in format_bits_float__rounding_list:
        self.assertEqual(bits, struct.pack(formatcode, f))
    format_bits_float__roundingError_list = [('>e', 65520.0), ('>e', 65536.0), ('>e', 1e+300), ('>e', -65520.0), ('>e', -65536.0), ('>e', -1e+300), ('<e', 65520.0), ('<e', 65536.0), ('<e', 1e+300), ('<e', -65520.0), ('<e', -65536.0), ('<e', -1e+300)]
    for (formatcode, f) in format_bits_float__roundingError_list:
        self.assertRaises(OverflowError, struct.pack, formatcode, f)
    format_bits_float__doubleRoundingError_list = [('>e', b'g\xff', 137405399039 * 2 ** (-26))]
    for (formatcode, bits, f) in format_bits_float__doubleRoundingError_list:
        self.assertEqual(bits, struct.pack(formatcode, f))
