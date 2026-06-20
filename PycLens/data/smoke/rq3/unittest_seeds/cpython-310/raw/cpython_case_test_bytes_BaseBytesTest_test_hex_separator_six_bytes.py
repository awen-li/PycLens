# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_hex_separator_six_bytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    six_bytes = self.type2test((x * 3 for x in range(1, 7)))
    self.assertEqual(six_bytes.hex(), '0306090c0f12')
    self.assertEqual(six_bytes.hex('.', 1), '03.06.09.0c.0f.12')
    self.assertEqual(six_bytes.hex(' ', 2), '0306 090c 0f12')
    self.assertEqual(six_bytes.hex('-', 3), '030609-0c0f12')
    self.assertEqual(six_bytes.hex(':', 4), '0306:090c0f12')
    self.assertEqual(six_bytes.hex(':', 5), '03:06090c0f12')
    self.assertEqual(six_bytes.hex(':', 6), '0306090c0f12')
    self.assertEqual(six_bytes.hex(':', 95), '0306090c0f12')
    self.assertEqual(six_bytes.hex('_', -3), '030609_0c0f12')
    self.assertEqual(six_bytes.hex(':', -4), '0306090c:0f12')
    self.assertEqual(six_bytes.hex(b'@', -5), '0306090c0f@12')
    self.assertEqual(six_bytes.hex(':', -6), '0306090c0f12')
    self.assertEqual(six_bytes.hex(' ', -95), '0306090c0f12')
