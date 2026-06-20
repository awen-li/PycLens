# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: FileTestCase_test_seekable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = LZMAFile(BytesIO(COMPRESSED_XZ))
    try:
        self.assertTrue(f.seekable())
        f.read()
        self.assertTrue(f.seekable())
    finally:
        f.close()
    self.assertRaises(ValueError, f.seekable)
    f = LZMAFile(BytesIO(), 'w')
    try:
        self.assertFalse(f.seekable())
    finally:
        f.close()
    self.assertRaises(ValueError, f.seekable)
    src = BytesIO(COMPRESSED_XZ)
    src.seekable = lambda : False
    f = LZMAFile(src)
    try:
        self.assertFalse(f.seekable())
    finally:
        f.close()
    self.assertRaises(ValueError, f.seekable)
