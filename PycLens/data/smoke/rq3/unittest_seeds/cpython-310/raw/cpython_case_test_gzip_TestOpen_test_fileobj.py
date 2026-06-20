# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gzip.py
# case: TestOpen_test_fileobj

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    uncompressed_bytes = data1 * 50
    uncompressed_str = uncompressed_bytes.decode('ascii')
    compressed = gzip.compress(uncompressed_bytes)
    with gzip.open(io.BytesIO(compressed), 'r') as f:
        self.assertEqual(f.read(), uncompressed_bytes)
    with gzip.open(io.BytesIO(compressed), 'rb') as f:
        self.assertEqual(f.read(), uncompressed_bytes)
    with gzip.open(io.BytesIO(compressed), 'rt', encoding='ascii') as f:
        self.assertEqual(f.read(), uncompressed_str)
