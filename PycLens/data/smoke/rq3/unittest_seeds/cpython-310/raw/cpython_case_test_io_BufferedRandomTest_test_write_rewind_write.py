# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedRandomTest_test_write_rewind_write

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def mutate(bufio, pos1, pos2):
        assert pos2 >= pos1
        bufio.seek(pos1)
        bufio.read(pos2 - pos1)
        bufio.write(b'\x02')
        bufio.seek(pos1)
        bufio.write(b'\x01')
    b = b'\x80\x81\x82\x83\x84'
    for i in range(0, len(b)):
        for j in range(i, len(b)):
            raw = self.BytesIO(b)
            bufio = self.tp(raw, 100)
            mutate(bufio, i, j)
            bufio.flush()
            expected = bytearray(b)
            expected[j] = 2
            expected[i] = 1
            self.assertEqual(raw.getvalue(), expected, 'failed result for i=%d, j=%d' % (i, j))
