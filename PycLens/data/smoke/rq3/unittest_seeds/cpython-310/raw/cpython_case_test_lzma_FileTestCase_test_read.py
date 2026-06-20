# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: FileTestCase_test_read

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with LZMAFile(BytesIO(COMPRESSED_XZ)) as f:
        self.assertEqual(f.read(), INPUT)
        self.assertEqual(f.read(), b'')
    with LZMAFile(BytesIO(COMPRESSED_ALONE)) as f:
        self.assertEqual(f.read(), INPUT)
    with LZMAFile(BytesIO(COMPRESSED_XZ), format=lzma.FORMAT_XZ) as f:
        self.assertEqual(f.read(), INPUT)
        self.assertEqual(f.read(), b'')
    with LZMAFile(BytesIO(COMPRESSED_ALONE), format=lzma.FORMAT_ALONE) as f:
        self.assertEqual(f.read(), INPUT)
        self.assertEqual(f.read(), b'')
    with LZMAFile(BytesIO(COMPRESSED_RAW_1), format=lzma.FORMAT_RAW, filters=FILTERS_RAW_1) as f:
        self.assertEqual(f.read(), INPUT)
        self.assertEqual(f.read(), b'')
    with LZMAFile(BytesIO(COMPRESSED_RAW_2), format=lzma.FORMAT_RAW, filters=FILTERS_RAW_2) as f:
        self.assertEqual(f.read(), INPUT)
        self.assertEqual(f.read(), b'')
    with LZMAFile(BytesIO(COMPRESSED_RAW_3), format=lzma.FORMAT_RAW, filters=FILTERS_RAW_3) as f:
        self.assertEqual(f.read(), INPUT)
        self.assertEqual(f.read(), b'')
    with LZMAFile(BytesIO(COMPRESSED_RAW_4), format=lzma.FORMAT_RAW, filters=FILTERS_RAW_4) as f:
        self.assertEqual(f.read(), INPUT)
        self.assertEqual(f.read(), b'')
