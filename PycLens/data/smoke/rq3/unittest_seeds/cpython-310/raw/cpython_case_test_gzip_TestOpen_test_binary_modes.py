# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gzip.py
# case: TestOpen_test_binary_modes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    uncompressed = data1 * 50
    with gzip.open(self.filename, 'wb') as f:
        f.write(uncompressed)
    with open(self.filename, 'rb') as f:
        file_data = gzip.decompress(f.read())
        self.assertEqual(file_data, uncompressed)
    with gzip.open(self.filename, 'rb') as f:
        self.assertEqual(f.read(), uncompressed)
    with gzip.open(self.filename, 'ab') as f:
        f.write(uncompressed)
    with open(self.filename, 'rb') as f:
        file_data = gzip.decompress(f.read())
        self.assertEqual(file_data, uncompressed * 2)
    with self.assertRaises(FileExistsError):
        gzip.open(self.filename, 'xb')
    os_helper.unlink(self.filename)
    with gzip.open(self.filename, 'xb') as f:
        f.write(uncompressed)
    with open(self.filename, 'rb') as f:
        file_data = gzip.decompress(f.read())
        self.assertEqual(file_data, uncompressed)
