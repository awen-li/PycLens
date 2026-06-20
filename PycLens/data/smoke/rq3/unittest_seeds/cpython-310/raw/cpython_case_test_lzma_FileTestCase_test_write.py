# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: FileTestCase_test_write

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with BytesIO() as dst:
        with LZMAFile(dst, 'w') as f:
            f.write(INPUT)
        expected = lzma.compress(INPUT)
        self.assertEqual(dst.getvalue(), expected)
    with BytesIO() as dst:
        with LZMAFile(dst, 'w', format=lzma.FORMAT_XZ) as f:
            f.write(INPUT)
        expected = lzma.compress(INPUT, format=lzma.FORMAT_XZ)
        self.assertEqual(dst.getvalue(), expected)
    with BytesIO() as dst:
        with LZMAFile(dst, 'w', format=lzma.FORMAT_ALONE) as f:
            f.write(INPUT)
        expected = lzma.compress(INPUT, format=lzma.FORMAT_ALONE)
        self.assertEqual(dst.getvalue(), expected)
    with BytesIO() as dst:
        with LZMAFile(dst, 'w', format=lzma.FORMAT_RAW, filters=FILTERS_RAW_2) as f:
            f.write(INPUT)
        expected = lzma.compress(INPUT, format=lzma.FORMAT_RAW, filters=FILTERS_RAW_2)
        self.assertEqual(dst.getvalue(), expected)
