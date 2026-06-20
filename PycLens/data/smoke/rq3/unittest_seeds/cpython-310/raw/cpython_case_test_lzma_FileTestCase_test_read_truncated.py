# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: FileTestCase_test_read_truncated

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    truncated = COMPRESSED_XZ[:-12]
    with LZMAFile(BytesIO(truncated)) as f:
        self.assertRaises(EOFError, f.read)
    with LZMAFile(BytesIO(truncated)) as f:
        self.assertEqual(f.read(len(INPUT)), INPUT)
        self.assertRaises(EOFError, f.read, 1)
    for i in range(12):
        with LZMAFile(BytesIO(truncated[:i])) as f:
            self.assertRaises(EOFError, f.read, 1)
