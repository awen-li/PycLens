# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: FileTestCase_test_writelines

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with BytesIO(INPUT) as f:
        lines = f.readlines()
    with BytesIO() as dst:
        with LZMAFile(dst, 'w') as f:
            f.writelines(lines)
        expected = lzma.compress(INPUT)
        self.assertEqual(dst.getvalue(), expected)
