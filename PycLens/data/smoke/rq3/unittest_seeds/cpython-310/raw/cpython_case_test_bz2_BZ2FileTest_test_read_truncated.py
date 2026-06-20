# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bz2.py
# case: BZ2FileTest_test_read_truncated

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    truncated = self.DATA[:-10]
    with BZ2File(BytesIO(truncated)) as f:
        self.assertRaises(EOFError, f.read)
    with BZ2File(BytesIO(truncated)) as f:
        self.assertEqual(f.read(len(self.TEXT)), self.TEXT)
        self.assertRaises(EOFError, f.read, 1)
    for i in range(22):
        with BZ2File(BytesIO(truncated[:i])) as f:
            self.assertRaises(EOFError, f.read, 1)
