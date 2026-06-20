# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: FileTestCase_test_tell

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with LZMAFile(BytesIO(COMPRESSED_XZ)) as f:
        pos = 0
        while True:
            self.assertEqual(f.tell(), pos)
            result = f.read(183)
            if not result:
                break
            pos += len(result)
        self.assertEqual(f.tell(), len(INPUT))
    with LZMAFile(BytesIO(), 'w') as f:
        for pos in range(0, len(INPUT), 144):
            self.assertEqual(f.tell(), pos)
            f.write(INPUT[pos:pos + 144])
        self.assertEqual(f.tell(), len(INPUT))
