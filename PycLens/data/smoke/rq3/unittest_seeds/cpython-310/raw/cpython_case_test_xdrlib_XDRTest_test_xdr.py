# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xdrlib.py
# case: XDRTest_test_xdr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = xdrlib.Packer()
    s = b'hello world'
    a = [b'what', b'is', b'hapnin', b'doctor']
    p.pack_int(42)
    p.pack_int(-17)
    p.pack_uint(9)
    p.pack_bool(True)
    p.pack_bool(False)
    p.pack_uhyper(45)
    p.pack_float(1.9)
    p.pack_double(1.9)
    p.pack_string(s)
    p.pack_list(range(5), p.pack_uint)
    p.pack_array(a, p.pack_string)
    data = p.get_buffer()
    up = xdrlib.Unpacker(data)
    self.assertEqual(up.get_position(), 0)
    self.assertEqual(up.unpack_int(), 42)
    self.assertEqual(up.unpack_int(), -17)
    self.assertEqual(up.unpack_uint(), 9)
    self.assertTrue(up.unpack_bool() is True)
    pos = up.get_position()
    self.assertTrue(up.unpack_bool() is False)
    up.set_position(pos)
    self.assertTrue(up.unpack_bool() is False)
    self.assertEqual(up.unpack_uhyper(), 45)
    self.assertAlmostEqual(up.unpack_float(), 1.9)
    self.assertAlmostEqual(up.unpack_double(), 1.9)
    self.assertEqual(up.unpack_string(), s)
    self.assertEqual(up.unpack_list(up.unpack_uint), list(range(5)))
    self.assertEqual(up.unpack_array(up.unpack_string), a)
    up.done()
    self.assertRaises(EOFError, up.unpack_uint)
