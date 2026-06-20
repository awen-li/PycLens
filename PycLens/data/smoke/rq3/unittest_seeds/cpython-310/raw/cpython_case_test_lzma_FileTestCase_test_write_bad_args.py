# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: FileTestCase_test_write_bad_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = LZMAFile(BytesIO(), 'w')
    f.close()
    self.assertRaises(ValueError, f.write, b'foo')
    with LZMAFile(BytesIO(COMPRESSED_XZ), 'r') as f:
        self.assertRaises(ValueError, f.write, b'bar')
    with LZMAFile(BytesIO(), 'w') as f:
        self.assertRaises(TypeError, f.write, None)
        self.assertRaises(TypeError, f.write, 'text')
        self.assertRaises(TypeError, f.write, 789)
