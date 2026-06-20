# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_audioop.py
# case: TestAudioop_test_bias

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for w in (1, 2, 3, 4):
        for bias in (0, 1, -1, 127, -128, 2147483647, -2147483648):
            self.assertEqual(audioop.bias(b'', w, bias), b'')
            self.assertEqual(audioop.bias(bytearray(), w, bias), b'')
            self.assertEqual(audioop.bias(memoryview(b''), w, bias), b'')
    self.assertEqual(audioop.bias(datas[1], 1, 1), b'\x01\x13F\xbc\x80\x81\x00')
    self.assertEqual(audioop.bias(datas[1], 1, -1), b'\xff\x11D\xba~\x7f\xfe')
    self.assertEqual(audioop.bias(datas[1], 1, 2147483647), b'\xff\x11D\xba~\x7f\xfe')
    self.assertEqual(audioop.bias(datas[1], 1, -2147483648), datas[1])
    self.assertEqual(audioop.bias(datas[2], 2, 1), packs[2](1, 4661, 17768, -17766, -32768, -32767, 0))
    self.assertEqual(audioop.bias(datas[2], 2, -1), packs[2](-1, 4659, 17766, -17768, 32766, 32767, -2))
    self.assertEqual(audioop.bias(datas[2], 2, 2147483647), packs[2](-1, 4659, 17766, -17768, 32766, 32767, -2))
    self.assertEqual(audioop.bias(datas[2], 2, -2147483648), datas[2])
    self.assertEqual(audioop.bias(datas[3], 3, 1), packs[3](1, 1193047, 4548490, -4548488, -8388608, -8388607, 0))
    self.assertEqual(audioop.bias(datas[3], 3, -1), packs[3](-1, 1193045, 4548488, -4548490, 8388606, 8388607, -2))
    self.assertEqual(audioop.bias(datas[3], 3, 2147483647), packs[3](-1, 1193045, 4548488, -4548490, 8388606, 8388607, -2))
    self.assertEqual(audioop.bias(datas[3], 3, -2147483648), datas[3])
    self.assertEqual(audioop.bias(datas[4], 4, 1), packs[4](1, 305419897, 1164413356, -1164413354, -2147483648, -2147483647, 0))
    self.assertEqual(audioop.bias(datas[4], 4, -1), packs[4](-1, 305419895, 1164413354, -1164413356, 2147483646, 2147483647, -2))
    self.assertEqual(audioop.bias(datas[4], 4, 2147483647), packs[4](2147483647, -1842063753, -983070294, 983070292, -2, -1, 2147483646))
    self.assertEqual(audioop.bias(datas[4], 4, -2147483648), packs[4](-2147483648, -1842063752, -983070293, 983070293, -1, 0, 2147483647))
