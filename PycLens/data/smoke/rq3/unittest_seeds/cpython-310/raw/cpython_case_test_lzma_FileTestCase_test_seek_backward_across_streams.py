# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: FileTestCase_test_seek_backward_across_streams

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with LZMAFile(BytesIO(COMPRESSED_XZ * 2)) as f:
        f.read(len(INPUT) + 333)
        f.seek(737)
        self.assertEqual(f.read(), INPUT[737:] + INPUT)
