# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: FileTestCase_test_seek_bad_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = LZMAFile(BytesIO(COMPRESSED_XZ))
    f.close()
    self.assertRaises(ValueError, f.seek, 0)
    with LZMAFile(BytesIO(), 'w') as f:
        self.assertRaises(ValueError, f.seek, 0)
    with LZMAFile(BytesIO(COMPRESSED_XZ)) as f:
        self.assertRaises(ValueError, f.seek, 0, 3)
        self.assertRaises((TypeError, ValueError), f.seek, 9, ())
        self.assertRaises(TypeError, f.seek, None)
        self.assertRaises(TypeError, f.seek, b'derp')
