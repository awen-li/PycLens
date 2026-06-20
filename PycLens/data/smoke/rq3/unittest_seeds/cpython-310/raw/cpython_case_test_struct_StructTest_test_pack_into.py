# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_struct.py
# case: StructTest_test_pack_into

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    test_string = b'Reykjavik rocks, eow!'
    writable_buf = array.array('b', b' ' * 100)
    fmt = '21s'
    s = struct.Struct(fmt)
    s.pack_into(writable_buf, 0, test_string)
    from_buf = writable_buf.tobytes()[:len(test_string)]
    self.assertEqual(from_buf, test_string)
    s.pack_into(writable_buf, 10, test_string)
    from_buf = writable_buf.tobytes()[:len(test_string) + 10]
    self.assertEqual(from_buf, test_string[:10] + test_string)
    small_buf = array.array('b', b' ' * 10)
    self.assertRaises((ValueError, struct.error), s.pack_into, small_buf, 0, test_string)
    self.assertRaises((ValueError, struct.error), s.pack_into, small_buf, 2, test_string)
    sb = small_buf
    self.assertRaises((TypeError, struct.error), struct.pack_into, b'', sb, None)
