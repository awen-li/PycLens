# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: FileTestCase_test_writable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = LZMAFile(BytesIO(COMPRESSED_XZ))
    try:
        self.assertFalse(f.writable())
        f.read()
        self.assertFalse(f.writable())
    finally:
        f.close()
    self.assertRaises(ValueError, f.writable)
    f = LZMAFile(BytesIO(), 'w')
    try:
        self.assertTrue(f.writable())
    finally:
        f.close()
    self.assertRaises(ValueError, f.writable)
