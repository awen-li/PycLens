# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: FileTestCase_test_read_multistream

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with LZMAFile(BytesIO(COMPRESSED_XZ * 5)) as f:
        self.assertEqual(f.read(), INPUT * 5)
    with LZMAFile(BytesIO(COMPRESSED_XZ + COMPRESSED_ALONE)) as f:
        self.assertEqual(f.read(), INPUT * 2)
    with LZMAFile(BytesIO(COMPRESSED_RAW_3 * 4), format=lzma.FORMAT_RAW, filters=FILTERS_RAW_3) as f:
        self.assertEqual(f.read(), INPUT * 4)
