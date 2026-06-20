# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gzip.py
# case: TestGzip_test_mtime

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    mtime = 123456789
    with gzip.GzipFile(self.filename, 'w', mtime=mtime) as fWrite:
        fWrite.write(data1)
    with gzip.GzipFile(self.filename) as fRead:
        self.assertTrue(hasattr(fRead, 'mtime'))
        self.assertIsNone(fRead.mtime)
        dataRead = fRead.read()
        self.assertEqual(dataRead, data1)
        self.assertEqual(fRead.mtime, mtime)
