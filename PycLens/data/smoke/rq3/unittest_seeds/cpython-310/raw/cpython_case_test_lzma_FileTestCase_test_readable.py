# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: FileTestCase_test_readable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = LZMAFile(BytesIO(COMPRESSED_XZ))
    try:
        self.assertTrue(f.readable())
        f.read()
        self.assertTrue(f.readable())
    finally:
        f.close()
    self.assertRaises(ValueError, f.readable)
    f = LZMAFile(BytesIO(), 'w')
    try:
        self.assertFalse(f.readable())
    finally:
        f.close()
    self.assertRaises(ValueError, f.readable)
