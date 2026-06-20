# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: FileTestCase_test_write_10

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with BytesIO() as dst:
        with LZMAFile(dst, 'w') as f:
            for start in range(0, len(INPUT), 10):
                f.write(INPUT[start:start + 10])
        expected = lzma.compress(INPUT)
        self.assertEqual(dst.getvalue(), expected)
