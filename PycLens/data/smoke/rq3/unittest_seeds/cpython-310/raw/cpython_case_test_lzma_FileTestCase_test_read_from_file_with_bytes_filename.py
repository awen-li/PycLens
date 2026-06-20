# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: FileTestCase_test_read_from_file_with_bytes_filename

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        bytes_filename = TESTFN.encode('ascii')
    except UnicodeEncodeError:
        self.skipTest('Temporary file name needs to be ASCII')
    with TempFile(TESTFN, COMPRESSED_XZ):
        with LZMAFile(bytes_filename) as f:
            self.assertEqual(f.read(), INPUT)
            self.assertEqual(f.read(), b'')
