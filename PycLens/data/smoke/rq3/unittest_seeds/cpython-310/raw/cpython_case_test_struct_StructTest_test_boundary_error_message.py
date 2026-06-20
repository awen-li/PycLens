# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_struct.py
# case: StructTest_test_boundary_error_message

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    regex1 = 'pack_into requires a buffer of at least 6 bytes for packing 1 bytes at offset 5 \\(actual buffer size is 1\\)'
    with self.assertRaisesRegex(struct.error, regex1):
        struct.pack_into('b', bytearray(1), 5, 1)
    regex2 = 'unpack_from requires a buffer of at least 6 bytes for unpacking 1 bytes at offset 5 \\(actual buffer size is 1\\)'
    with self.assertRaisesRegex(struct.error, regex2):
        struct.unpack_from('b', bytearray(1), 5)
