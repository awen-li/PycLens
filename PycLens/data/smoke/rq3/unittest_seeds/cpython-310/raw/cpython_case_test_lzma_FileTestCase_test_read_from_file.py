# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: FileTestCase_test_read_from_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with TempFile(TESTFN, COMPRESSED_XZ):
        with LZMAFile(TESTFN) as f:
            self.assertEqual(f.read(), INPUT)
            self.assertEqual(f.read(), b'')
