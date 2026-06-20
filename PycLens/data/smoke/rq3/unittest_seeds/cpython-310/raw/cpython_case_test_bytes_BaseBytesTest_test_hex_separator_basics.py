# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_hex_separator_basics

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    three_bytes = self.type2test(b'\xb9\x01\xef')
    self.assertEqual(three_bytes.hex(), 'b901ef')
    with self.assertRaises(ValueError):
        three_bytes.hex('')
    with self.assertRaises(ValueError):
        three_bytes.hex('xx')
    self.assertEqual(three_bytes.hex(':', 0), 'b901ef')
    with self.assertRaises(TypeError):
        three_bytes.hex(None, 0)
    with self.assertRaises(ValueError):
        three_bytes.hex('ÿ')
    with self.assertRaises(ValueError):
        three_bytes.hex(b'\xff')
    with self.assertRaises(ValueError):
        three_bytes.hex(b'\x80')
    with self.assertRaises(ValueError):
        three_bytes.hex(chr(256))
    self.assertEqual(three_bytes.hex(':', 0), 'b901ef')
    self.assertEqual(three_bytes.hex(b'\x00'), 'b9\x0001\x00ef')
    self.assertEqual(three_bytes.hex('\x00'), 'b9\x0001\x00ef')
    self.assertEqual(three_bytes.hex(b'\x7f'), 'b9\x7f01\x7fef')
    self.assertEqual(three_bytes.hex('\x7f'), 'b9\x7f01\x7fef')
    self.assertEqual(three_bytes.hex(':', 3), 'b901ef')
    self.assertEqual(three_bytes.hex(':', 4), 'b901ef')
    self.assertEqual(three_bytes.hex(':', -4), 'b901ef')
    self.assertEqual(three_bytes.hex(':'), 'b9:01:ef')
    self.assertEqual(three_bytes.hex(b'$'), 'b9$01$ef')
    self.assertEqual(three_bytes.hex(':', 1), 'b9:01:ef')
    self.assertEqual(three_bytes.hex(':', -1), 'b9:01:ef')
    self.assertEqual(three_bytes.hex(':', 2), 'b9:01ef')
    self.assertEqual(three_bytes.hex(':', 1), 'b9:01:ef')
    self.assertEqual(three_bytes.hex('*', -2), 'b901*ef')
    value = b'{s\x05\x00\x00\x00worldi\x02\x00\x00\x00s\x05\x00\x00\x00helloi\x01\x00\x00\x000'
    self.assertEqual(value.hex('.', 8), '7b7305000000776f.726c646902000000.730500000068656c.6c6f690100000030')
