# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gzip.py
# case: TestOpen_test_text_modes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    uncompressed = data1.decode('ascii') * 50
    uncompressed_raw = uncompressed.replace('\n', os.linesep)
    with gzip.open(self.filename, 'wt', encoding='ascii') as f:
        f.write(uncompressed)
    with open(self.filename, 'rb') as f:
        file_data = gzip.decompress(f.read()).decode('ascii')
        self.assertEqual(file_data, uncompressed_raw)
    with gzip.open(self.filename, 'rt', encoding='ascii') as f:
        self.assertEqual(f.read(), uncompressed)
    with gzip.open(self.filename, 'at', encoding='ascii') as f:
        f.write(uncompressed)
    with open(self.filename, 'rb') as f:
        file_data = gzip.decompress(f.read()).decode('ascii')
        self.assertEqual(file_data, uncompressed_raw * 2)
