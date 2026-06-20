# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_struct.py
# case: StructTest_test_trailing_counter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    store = array.array('b', b' ' * 100)
    self.assertRaises(struct.error, struct.pack, '12345')
    self.assertRaises(struct.error, struct.unpack, '12345', b'')
    self.assertRaises(struct.error, struct.pack_into, '12345', store, 0)
    self.assertRaises(struct.error, struct.unpack_from, '12345', store, 0)
    self.assertRaises(struct.error, struct.pack, 'c12345', 'x')
    self.assertRaises(struct.error, struct.unpack, 'c12345', b'x')
    self.assertRaises(struct.error, struct.pack_into, 'c12345', store, 0, 'x')
    self.assertRaises(struct.error, struct.unpack_from, 'c12345', store, 0)
    self.assertRaises(struct.error, struct.pack, '14s42', 'spam and eggs')
    self.assertRaises(struct.error, struct.unpack, '14s42', b'spam and eggs')
    self.assertRaises(struct.error, struct.pack_into, '14s42', store, 0, 'spam and eggs')
    self.assertRaises(struct.error, struct.unpack_from, '14s42', store, 0)
