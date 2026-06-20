# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: FileTestCase_test_init_bad_filter_spec

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError):
        LZMAFile(BytesIO(), 'w', filters=[b'wobsite'])
    with self.assertRaises(ValueError):
        LZMAFile(BytesIO(), 'w', filters=[{'xyzzy': 3}])
    with self.assertRaises(ValueError):
        LZMAFile(BytesIO(), 'w', filters=[{'id': 98765}])
    with self.assertRaises(ValueError):
        LZMAFile(BytesIO(), 'w', filters=[{'id': lzma.FILTER_LZMA2, 'foo': 0}])
    with self.assertRaises(ValueError):
        LZMAFile(BytesIO(), 'w', filters=[{'id': lzma.FILTER_DELTA, 'foo': 0}])
    with self.assertRaises(ValueError):
        LZMAFile(BytesIO(), 'w', filters=[{'id': lzma.FILTER_X86, 'foo': 0}])
