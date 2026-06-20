# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gzip.py
# case: TestGzip_test_peek

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    uncompressed = data1 * 200
    with gzip.GzipFile(self.filename, 'wb') as f:
        f.write(uncompressed)

    def sizes():
        while True:
            for n in range(5, 50, 10):
                yield n
    with gzip.GzipFile(self.filename, 'rb') as f:
        f.max_read_chunk = 33
        nread = 0
        for n in sizes():
            s = f.peek(n)
            if s == b'':
                break
            self.assertEqual(f.read(len(s)), s)
            nread += len(s)
        self.assertEqual(f.read(100), b'')
        self.assertEqual(nread, len(uncompressed))
