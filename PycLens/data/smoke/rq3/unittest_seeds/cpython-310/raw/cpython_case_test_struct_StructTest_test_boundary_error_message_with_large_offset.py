# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_struct.py
# case: StructTest_test_boundary_error_message_with_large_offset

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    regex1 = 'pack_into requires a buffer of at least ' + str(sys.maxsize + 4) + ' bytes for packing 4 bytes at offset ' + str(sys.maxsize) + ' \\(actual buffer size is 10\\)'
    with self.assertRaisesRegex(struct.error, regex1):
        struct.pack_into('<I', bytearray(10), sys.maxsize, 1)
    regex2 = 'unpack_from requires a buffer of at least ' + str(sys.maxsize + 4) + ' bytes for unpacking 4 bytes at offset ' + str(sys.maxsize) + ' \\(actual buffer size is 10\\)'
    with self.assertRaisesRegex(struct.error, regex2):
        struct.unpack_from('<I', bytearray(10), sys.maxsize)
