# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: ExtractTests_test_extract

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with temp_cwd():
        self.make_test_file()
        with zipfile.ZipFile(TESTFN2, 'r') as zipfp:
            for (fpath, fdata) in SMALL_TEST_DATA:
                writtenfile = zipfp.extract(fpath)
                correctfile = os.path.join(os.getcwd(), fpath)
                correctfile = os.path.normpath(correctfile)
                self.assertEqual(writtenfile, correctfile)
                with open(writtenfile, 'rb') as f:
                    self.assertEqual(fdata.encode(), f.read())
                unlink(writtenfile)
