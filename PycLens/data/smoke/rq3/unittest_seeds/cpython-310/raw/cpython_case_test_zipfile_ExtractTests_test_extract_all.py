# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: ExtractTests_test_extract_all

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with temp_cwd():
        self.make_test_file()
        with zipfile.ZipFile(TESTFN2, 'r') as zipfp:
            zipfp.extractall()
            for (fpath, fdata) in SMALL_TEST_DATA:
                outfile = os.path.join(os.getcwd(), fpath)
                with open(outfile, 'rb') as f:
                    self.assertEqual(fdata.encode(), f.read())
                unlink(outfile)
