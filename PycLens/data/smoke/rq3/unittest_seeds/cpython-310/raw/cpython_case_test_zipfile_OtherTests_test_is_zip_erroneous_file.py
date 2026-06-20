# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: OtherTests_test_is_zip_erroneous_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(TESTFN, 'w', encoding='utf-8') as fp:
        fp.write('this is not a legal zip file\n')
    self.assertFalse(zipfile.is_zipfile(TESTFN))
    self.assertFalse(zipfile.is_zipfile(pathlib.Path(TESTFN)))
    with open(TESTFN, 'rb') as fp:
        self.assertFalse(zipfile.is_zipfile(fp))
    fp = io.BytesIO()
    fp.write(b'this is not a legal zip file\n')
    self.assertFalse(zipfile.is_zipfile(fp))
    fp.seek(0, 0)
    self.assertFalse(zipfile.is_zipfile(fp))
