# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: FileTestCase_test_read_bad_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = LZMAFile(BytesIO(COMPRESSED_XZ))
    f.close()
    self.assertRaises(ValueError, f.read)
    with LZMAFile(BytesIO(), 'w') as f:
        self.assertRaises(ValueError, f.read)
    with LZMAFile(BytesIO(COMPRESSED_XZ)) as f:
        self.assertRaises(TypeError, f.read, float())
