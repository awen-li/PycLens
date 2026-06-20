# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gzip.py
# case: TestGzip_test_many_append

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with gzip.GzipFile(self.filename, 'wb', 9) as f:
        f.write(b'a')
    for i in range(0, 200):
        with gzip.GzipFile(self.filename, 'ab', 9) as f:
            f.write(b'a')
    with gzip.GzipFile(self.filename, 'rb') as zgfile:
        contents = b''
        while 1:
            ztxt = zgfile.read(8192)
            contents += ztxt
            if not ztxt:
                break
    self.assertEqual(contents, b'a' * 201)
