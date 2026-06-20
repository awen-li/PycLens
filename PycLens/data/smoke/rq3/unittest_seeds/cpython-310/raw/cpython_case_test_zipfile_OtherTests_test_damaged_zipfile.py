# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: OtherTests_test_damaged_zipfile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fp = io.BytesIO()
    with zipfile.ZipFile(fp, mode='w') as zipf:
        zipf.writestr('foo.txt', b'O, for a Muse of Fire!')
    zipfiledata = fp.getvalue()
    for N in range(len(zipfiledata)):
        fp = io.BytesIO(zipfiledata[:N])
        self.assertRaises(zipfile.BadZipFile, zipfile.ZipFile, fp)
