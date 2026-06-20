# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: FileTestCase_test_read_10

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with LZMAFile(BytesIO(COMPRESSED_XZ)) as f:
        chunks = []
        while True:
            result = f.read(10)
            if not result:
                break
            self.assertLessEqual(len(result), 10)
            chunks.append(result)
        self.assertEqual(b''.join(chunks), INPUT)
