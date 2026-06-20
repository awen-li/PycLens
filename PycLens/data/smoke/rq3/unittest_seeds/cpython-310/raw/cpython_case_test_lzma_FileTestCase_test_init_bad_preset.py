# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: FileTestCase_test_init_bad_preset

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError):
        LZMAFile(BytesIO(), 'w', preset=4.39)
    with self.assertRaises(LZMAError):
        LZMAFile(BytesIO(), 'w', preset=10)
    with self.assertRaises(LZMAError):
        LZMAFile(BytesIO(), 'w', preset=23)
    with self.assertRaises(OverflowError):
        LZMAFile(BytesIO(), 'w', preset=-1)
    with self.assertRaises(OverflowError):
        LZMAFile(BytesIO(), 'w', preset=-7)
    with self.assertRaises(TypeError):
        LZMAFile(BytesIO(), 'w', preset='foo')
    with self.assertRaises(ValueError):
        LZMAFile(BytesIO(COMPRESSED_XZ), preset=3)
