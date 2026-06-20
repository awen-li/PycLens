# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: FileTestCase_test_write_to_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        with LZMAFile(TESTFN, 'w') as f:
            f.write(INPUT)
        expected = lzma.compress(INPUT)
        with open(TESTFN, 'rb') as f:
            self.assertEqual(f.read(), expected)
    finally:
        unlink(TESTFN)
