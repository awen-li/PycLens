# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: OtherTests_test_is_zip_valid_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with zipfile.ZipFile(TESTFN, mode='w') as zipf:
        zipf.writestr('foo.txt', b'O, for a Muse of Fire!')
    self.assertTrue(zipfile.is_zipfile(TESTFN))
    with open(TESTFN, 'rb') as fp:
        self.assertTrue(zipfile.is_zipfile(fp))
        fp.seek(0, 0)
        zip_contents = fp.read()
    fp = io.BytesIO()
    fp.write(zip_contents)
    self.assertTrue(zipfile.is_zipfile(fp))
    fp.seek(0, 0)
    self.assertTrue(zipfile.is_zipfile(fp))
