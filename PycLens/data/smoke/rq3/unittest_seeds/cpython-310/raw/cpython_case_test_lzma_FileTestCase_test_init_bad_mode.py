# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: FileTestCase_test_init_bad_mode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(ValueError):
        LZMAFile(BytesIO(COMPRESSED_XZ), (3, 'x'))
    with self.assertRaises(ValueError):
        LZMAFile(BytesIO(COMPRESSED_XZ), '')
    with self.assertRaises(ValueError):
        LZMAFile(BytesIO(COMPRESSED_XZ), 'xt')
    with self.assertRaises(ValueError):
        LZMAFile(BytesIO(COMPRESSED_XZ), 'x+')
    with self.assertRaises(ValueError):
        LZMAFile(BytesIO(COMPRESSED_XZ), 'rx')
    with self.assertRaises(ValueError):
        LZMAFile(BytesIO(COMPRESSED_XZ), 'wx')
    with self.assertRaises(ValueError):
        LZMAFile(BytesIO(COMPRESSED_XZ), 'rt')
    with self.assertRaises(ValueError):
        LZMAFile(BytesIO(COMPRESSED_XZ), 'r+')
    with self.assertRaises(ValueError):
        LZMAFile(BytesIO(COMPRESSED_XZ), 'wt')
    with self.assertRaises(ValueError):
        LZMAFile(BytesIO(COMPRESSED_XZ), 'w+')
    with self.assertRaises(ValueError):
        LZMAFile(BytesIO(COMPRESSED_XZ), 'rw')
