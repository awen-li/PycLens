# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: FileTestCase_test_close

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with BytesIO(COMPRESSED_XZ) as src:
        f = LZMAFile(src)
        f.close()
        self.assertFalse(src.closed)
        f.close()
        self.assertFalse(src.closed)
    with TempFile(TESTFN, COMPRESSED_XZ):
        f = LZMAFile(TESTFN)
        fp = f._fp
        f.close()
        self.assertTrue(fp.closed)
        f.close()
