# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: FileTestCase_test_closed

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = LZMAFile(BytesIO(COMPRESSED_XZ))
    try:
        self.assertFalse(f.closed)
        f.read()
        self.assertFalse(f.closed)
    finally:
        f.close()
    self.assertTrue(f.closed)
    f = LZMAFile(BytesIO(), 'w')
    try:
        self.assertFalse(f.closed)
    finally:
        f.close()
    self.assertTrue(f.closed)
