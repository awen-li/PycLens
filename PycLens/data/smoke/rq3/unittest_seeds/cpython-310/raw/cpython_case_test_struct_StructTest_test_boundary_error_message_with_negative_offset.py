# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_struct.py
# case: StructTest_test_boundary_error_message_with_negative_offset

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    byte_list = bytearray(10)
    with self.assertRaisesRegex(struct.error, 'no space to pack 4 bytes at offset -2'):
        struct.pack_into('<I', byte_list, -2, 123)
    with self.assertRaisesRegex(struct.error, 'offset -11 out of range for 10-byte buffer'):
        struct.pack_into('<B', byte_list, -11, 123)
    with self.assertRaisesRegex(struct.error, 'not enough data to unpack 4 bytes at offset -2'):
        struct.unpack_from('<I', byte_list, -2)
    with self.assertRaisesRegex(struct.error, 'offset -11 out of range for 10-byte buffer'):
        struct.unpack_from('<B', byte_list, -11)
