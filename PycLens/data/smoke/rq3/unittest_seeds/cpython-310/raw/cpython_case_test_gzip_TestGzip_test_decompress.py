# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gzip.py
# case: TestGzip_test_decompress

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for data in (data1, data2):
        buf = io.BytesIO()
        with gzip.GzipFile(fileobj=buf, mode='wb') as f:
            f.write(data)
        self.assertEqual(gzip.decompress(buf.getvalue()), data)
        datac = gzip.compress(data)
        self.assertEqual(gzip.decompress(datac), data)
