# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: FileTestCase_test_readline

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with BytesIO(INPUT) as f:
        lines = f.readlines()
    with LZMAFile(BytesIO(COMPRESSED_XZ)) as f:
        for line in lines:
            self.assertEqual(f.readline(), line)
