# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: AbstractTestsWithSourceFile_test_open_with_pathlike

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    path = pathlib.Path(TESTFN2)
    self.zip_open_test(path, self.compression)
    with zipfile.ZipFile(path, 'r', self.compression) as zipfp:
        self.assertIsInstance(zipfp.filename, str)
