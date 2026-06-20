# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: AbstractBadCrcTests_test_testzip_with_bad_crc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    zipdata = self.zip_with_bad_crc
    with zipfile.ZipFile(io.BytesIO(zipdata), mode='r') as zipf:
        self.assertEqual('afile', zipf.testzip())
