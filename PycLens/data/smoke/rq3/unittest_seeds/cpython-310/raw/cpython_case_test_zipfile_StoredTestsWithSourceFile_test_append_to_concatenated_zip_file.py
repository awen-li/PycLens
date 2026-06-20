# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: StoredTestsWithSourceFile_test_append_to_concatenated_zip_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with io.BytesIO() as bio:
        with zipfile.ZipFile(bio, 'w', zipfile.ZIP_STORED) as zipfp:
            zipfp.write(TESTFN, TESTFN)
        zipfiledata = bio.getvalue()
    data = b'I am not a ZipFile!' * 1000000
    with open(TESTFN2, 'wb') as f:
        f.write(data)
        f.write(zipfiledata)
    with zipfile.ZipFile(TESTFN2, 'a') as zipfp:
        self.assertEqual(zipfp.namelist(), [TESTFN])
        zipfp.writestr('strfile', self.data)
    with open(TESTFN2, 'rb') as f:
        self.assertEqual(f.read(len(data)), data)
        zipfiledata = f.read()
    with io.BytesIO(zipfiledata) as bio, zipfile.ZipFile(bio) as zipfp:
        self.assertEqual(zipfp.namelist(), [TESTFN, 'strfile'])
        self.assertEqual(zipfp.read(TESTFN), self.data)
        self.assertEqual(zipfp.read('strfile'), self.data)
