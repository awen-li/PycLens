# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: StoredTestsWithSourceFile_test_append_to_non_zip_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = b'I am not a ZipFile!' * 10
    with open(TESTFN2, 'wb') as f:
        f.write(data)
    with zipfile.ZipFile(TESTFN2, 'a', zipfile.ZIP_STORED) as zipfp:
        zipfp.write(TESTFN, TESTFN)
    with open(TESTFN2, 'rb') as f:
        f.seek(len(data))
        with zipfile.ZipFile(f, 'r') as zipfp:
            self.assertEqual(zipfp.namelist(), [TESTFN])
            self.assertEqual(zipfp.read(TESTFN), self.data)
    with open(TESTFN2, 'rb') as f:
        self.assertEqual(f.read(len(data)), data)
        zipfiledata = f.read()
    with io.BytesIO(zipfiledata) as bio, zipfile.ZipFile(bio) as zipfp:
        self.assertEqual(zipfp.namelist(), [TESTFN])
        self.assertEqual(zipfp.read(TESTFN), self.data)
