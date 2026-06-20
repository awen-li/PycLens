# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_struct.py
# case: StructTest_test_consistence

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(struct.error, struct.calcsize, 'Z')
    sz = struct.calcsize('i')
    self.assertEqual(sz * 3, struct.calcsize('iii'))
    fmt = 'cbxxxxxxhhhhiillffd?'
    fmt3 = '3c3b18x12h6i6l6f3d3?'
    sz = struct.calcsize(fmt)
    sz3 = struct.calcsize(fmt3)
    self.assertEqual(sz * 3, sz3)
    self.assertRaises(struct.error, struct.pack, 'iii', 3)
    self.assertRaises(struct.error, struct.pack, 'i', 3, 3, 3)
    self.assertRaises((TypeError, struct.error), struct.pack, 'i', 'foo')
    self.assertRaises((TypeError, struct.error), struct.pack, 'P', 'foo')
    self.assertRaises(struct.error, struct.unpack, 'd', b'flap')
    s = struct.pack('ii', 1, 2)
    self.assertRaises(struct.error, struct.unpack, 'iii', s)
    self.assertRaises(struct.error, struct.unpack, 'i', s)
