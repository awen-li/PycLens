# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gzip.py
# case: TestGzip_test_compresslevel_metadata

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cases = [('fast', 1, b'\x04'), ('best', 9, b'\x02'), ('tradeoff', 6, b'\x00')]
    xflOffset = 8
    for (name, level, expectedXflByte) in cases:
        with self.subTest(name):
            fWrite = gzip.GzipFile(self.filename, 'w', compresslevel=level)
            with fWrite:
                fWrite.write(data1)
            with open(self.filename, 'rb') as fRead:
                fRead.seek(xflOffset)
                xflByte = fRead.read(1)
                self.assertEqual(xflByte, expectedXflByte)
