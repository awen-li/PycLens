# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: FileTestCase_test_init_with_PathLike_filename

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    filename = pathlib.Path(TESTFN)
    with TempFile(filename, COMPRESSED_XZ):
        with LZMAFile(filename) as f:
            self.assertEqual(f.read(), INPUT)
        with LZMAFile(filename, 'a') as f:
            f.write(INPUT)
        with LZMAFile(filename) as f:
            self.assertEqual(f.read(), INPUT * 2)
