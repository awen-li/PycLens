# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: FileTestCase_test_fileno

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = LZMAFile(BytesIO(COMPRESSED_XZ))
    try:
        self.assertRaises(UnsupportedOperation, f.fileno)
    finally:
        f.close()
    self.assertRaises(ValueError, f.fileno)
    with TempFile(TESTFN, COMPRESSED_XZ):
        f = LZMAFile(TESTFN)
        try:
            self.assertEqual(f.fileno(), f._fp.fileno())
            self.assertIsInstance(f.fileno(), int)
        finally:
            f.close()
    self.assertRaises(ValueError, f.fileno)
