# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gzip.py
# case: TestGzip_test_read1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.test_write()
    blocks = []
    nread = 0
    with gzip.GzipFile(self.filename, 'r') as f:
        while True:
            d = f.read1()
            if not d:
                break
            blocks.append(d)
            nread += len(d)
            self.assertEqual(f.tell(), nread)
    self.assertEqual(b''.join(blocks), data1 * 50)
