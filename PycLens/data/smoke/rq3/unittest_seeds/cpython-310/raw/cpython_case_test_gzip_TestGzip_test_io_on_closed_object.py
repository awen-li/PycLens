# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gzip.py
# case: TestGzip_test_io_on_closed_object

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.test_write()
    f = gzip.GzipFile(self.filename, 'r')
    fileobj = f.fileobj
    self.assertFalse(fileobj.closed)
    f.close()
    self.assertTrue(fileobj.closed)
    with self.assertRaises(ValueError):
        f.read(1)
    with self.assertRaises(ValueError):
        f.seek(0)
    with self.assertRaises(ValueError):
        f.tell()
    f = gzip.GzipFile(self.filename, 'w')
    fileobj = f.fileobj
    self.assertFalse(fileobj.closed)
    f.close()
    self.assertTrue(fileobj.closed)
    with self.assertRaises(ValueError):
        f.write(b'')
    with self.assertRaises(ValueError):
        f.flush()
