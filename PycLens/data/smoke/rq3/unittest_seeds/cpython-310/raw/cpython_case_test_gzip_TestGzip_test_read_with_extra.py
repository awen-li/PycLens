# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gzip.py
# case: TestGzip_test_read_with_extra

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    gzdata = b'\x1f\x8b\x08\x04\xb2\x17cQ\x02\xff\x05\x00Extra\x0bI-.\x01\x002\xd1Mx\x04\x00\x00\x00'
    with gzip.GzipFile(fileobj=io.BytesIO(gzdata)) as f:
        self.assertEqual(f.read(), b'Test')
