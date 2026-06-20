# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gzip.py
# case: TestGzip_test_compress_mtime

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    mtime = 123456789
    for data in [data1, data2]:
        for args in [(), (1,), (6,), (9,)]:
            with self.subTest(data=data, args=args):
                datac = gzip.compress(data, *args, mtime=mtime)
                self.assertEqual(type(datac), bytes)
                with gzip.GzipFile(fileobj=io.BytesIO(datac), mode='rb') as f:
                    f.read(1)
                    self.assertEqual(f.mtime, mtime)
