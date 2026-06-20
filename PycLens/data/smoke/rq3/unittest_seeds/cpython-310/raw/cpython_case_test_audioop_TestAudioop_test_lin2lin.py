# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_audioop.py
# case: TestAudioop_test_lin2lin

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for w in (1, 2, 3, 4):
        self.assertEqual(audioop.lin2lin(datas[w], w, w), datas[w])
        self.assertEqual(audioop.lin2lin(bytearray(datas[w]), w, w), datas[w])
        self.assertEqual(audioop.lin2lin(memoryview(datas[w]), w, w), datas[w])
    self.assertEqual(audioop.lin2lin(datas[1], 1, 2), packs[2](0, 4608, 17664, -17664, 32512, -32768, -256))
    self.assertEqual(audioop.lin2lin(datas[1], 1, 3), packs[3](0, 1179648, 4521984, -4521984, 8323072, -8388608, -65536))
    self.assertEqual(audioop.lin2lin(datas[1], 1, 4), packs[4](0, 301989888, 1157627904, -1157627904, 2130706432, -2147483648, -16777216))
    self.assertEqual(audioop.lin2lin(datas[2], 2, 1), b'\x00\x12E\xba\x7f\x80\xff')
    self.assertEqual(audioop.lin2lin(datas[2], 2, 3), packs[3](0, 1192960, 4548352, -4548352, 8388352, -8388608, -256))
    self.assertEqual(audioop.lin2lin(datas[2], 2, 4), packs[4](0, 305397760, 1164378112, -1164378112, 2147418112, -2147483648, -65536))
    self.assertEqual(audioop.lin2lin(datas[3], 3, 1), b'\x00\x12E\xba\x7f\x80\xff')
    self.assertEqual(audioop.lin2lin(datas[3], 3, 2), packs[2](0, 4660, 17767, -17768, 32767, -32768, -1))
    self.assertEqual(audioop.lin2lin(datas[3], 3, 4), packs[4](0, 305419776, 1164413184, -1164413184, 2147483392, -2147483648, -256))
    self.assertEqual(audioop.lin2lin(datas[4], 4, 1), b'\x00\x12E\xba\x7f\x80\xff')
    self.assertEqual(audioop.lin2lin(datas[4], 4, 2), packs[2](0, 4660, 17767, -17768, 32767, -32768, -1))
    self.assertEqual(audioop.lin2lin(datas[4], 4, 3), packs[3](0, 1193046, 4548489, -4548490, 8388607, -8388608, -1))
