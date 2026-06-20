# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: TestWithDirectory_test_extract_dir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with zipfile.ZipFile(findfile('zipdir.zip')) as zipf:
        zipf.extractall(TESTFN2)
    self.assertTrue(os.path.isdir(os.path.join(TESTFN2, 'a')))
    self.assertTrue(os.path.isdir(os.path.join(TESTFN2, 'a', 'b')))
    self.assertTrue(os.path.exists(os.path.join(TESTFN2, 'a', 'b', 'c')))
