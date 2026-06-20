# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: FileTestCase_test_peek

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with LZMAFile(BytesIO(COMPRESSED_XZ)) as f:
        result = f.peek()
        self.assertGreater(len(result), 0)
        self.assertTrue(INPUT.startswith(result))
        self.assertEqual(f.read(), INPUT)
    with LZMAFile(BytesIO(COMPRESSED_XZ)) as f:
        result = f.peek(10)
        self.assertGreater(len(result), 0)
        self.assertTrue(INPUT.startswith(result))
        self.assertEqual(f.read(), INPUT)
