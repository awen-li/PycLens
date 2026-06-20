# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: FileTestCase_test_read1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with LZMAFile(BytesIO(COMPRESSED_XZ)) as f:
        blocks = []
        while True:
            result = f.read1()
            if not result:
                break
            blocks.append(result)
        self.assertEqual(b''.join(blocks), INPUT)
        self.assertEqual(f.read1(), b'')
