# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_audioop.py
# case: TestAudioop_test_mul

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for w in (1, 2, 3, 4):
        self.assertEqual(audioop.mul(b'', w, 2), b'')
        self.assertEqual(audioop.mul(bytearray(), w, 2), b'')
        self.assertEqual(audioop.mul(memoryview(b''), w, 2), b'')
        self.assertEqual(audioop.mul(datas[w], w, 0), b'\x00' * len(datas[w]))
        self.assertEqual(audioop.mul(datas[w], w, 1), datas[w])
    self.assertEqual(audioop.mul(datas[1], 1, 2), b'\x00$\x7f\x80\x7f\x80\xfe')
    self.assertEqual(audioop.mul(datas[2], 2, 2), packs[2](0, 9320, 32767, -32768, 32767, -32768, -2))
    self.assertEqual(audioop.mul(datas[3], 3, 2), packs[3](0, 2386092, 8388607, -8388608, 8388607, -8388608, -2))
    self.assertEqual(audioop.mul(datas[4], 4, 2), packs[4](0, 610839792, 2147483647, -2147483648, 2147483647, -2147483648, -2))
