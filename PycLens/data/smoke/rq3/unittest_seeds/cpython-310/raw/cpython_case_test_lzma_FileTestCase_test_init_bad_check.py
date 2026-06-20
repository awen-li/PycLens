# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: FileTestCase_test_init_bad_check

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError):
        LZMAFile(BytesIO(), 'w', check=b'asd')
    with self.assertRaises(LZMAError):
        LZMAFile(BytesIO(), 'w', check=lzma.CHECK_UNKNOWN)
    with self.assertRaises(LZMAError):
        LZMAFile(BytesIO(), 'w', check=lzma.CHECK_ID_MAX + 3)
    with self.assertRaises(ValueError):
        LZMAFile(BytesIO(COMPRESSED_XZ), check=lzma.CHECK_NONE)
    with self.assertRaises(ValueError):
        LZMAFile(BytesIO(COMPRESSED_XZ), check=lzma.CHECK_CRC32)
    with self.assertRaises(ValueError):
        LZMAFile(BytesIO(COMPRESSED_XZ), check=lzma.CHECK_CRC64)
    with self.assertRaises(ValueError):
        LZMAFile(BytesIO(COMPRESSED_XZ), check=lzma.CHECK_SHA256)
    with self.assertRaises(ValueError):
        LZMAFile(BytesIO(COMPRESSED_XZ), check=lzma.CHECK_UNKNOWN)
