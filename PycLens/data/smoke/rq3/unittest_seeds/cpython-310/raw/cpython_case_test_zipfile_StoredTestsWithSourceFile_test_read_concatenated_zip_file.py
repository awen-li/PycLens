# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: StoredTestsWithSourceFile_test_read_concatenated_zip_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with io.BytesIO() as bio:
        with zipfile.ZipFile(bio, 'w', zipfile.ZIP_STORED) as zipfp:
            zipfp.write(TESTFN, TESTFN)
        zipfiledata = bio.getvalue()
    data = b'I am not a ZipFile!' * 10
    with open(TESTFN2, 'wb') as f:
        f.write(data)
        f.write(zipfiledata)
    with zipfile.ZipFile(TESTFN2) as zipfp:
        self.assertEqual(zipfp.namelist(), [TESTFN])
        self.assertEqual(zipfp.read(TESTFN), self.data)
