# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_audioop.py
# case: TestAudioop_test_ratecv

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for w in (1, 2, 3, 4):
        self.assertEqual(audioop.ratecv(b'', w, 1, 8000, 8000, None), (b'', (-1, ((0, 0),))))
        self.assertEqual(audioop.ratecv(bytearray(), w, 1, 8000, 8000, None), (b'', (-1, ((0, 0),))))
        self.assertEqual(audioop.ratecv(memoryview(b''), w, 1, 8000, 8000, None), (b'', (-1, ((0, 0),))))
        self.assertEqual(audioop.ratecv(b'', w, 5, 8000, 8000, None), (b'', (-1, ((0, 0),) * 5)))
        self.assertEqual(audioop.ratecv(b'', w, 1, 8000, 16000, None), (b'', (-2, ((0, 0),))))
        self.assertEqual(audioop.ratecv(datas[w], w, 1, 8000, 8000, None)[0], datas[w])
        self.assertEqual(audioop.ratecv(datas[w], w, 1, 8000, 8000, None, 1, 0)[0], datas[w])
    state = None
    (d1, state) = audioop.ratecv(b'\x00\x01\x02', 1, 1, 8000, 16000, state)
    (d2, state) = audioop.ratecv(b'\x00\x01\x02', 1, 1, 8000, 16000, state)
    self.assertEqual(d1 + d2, b'\x00\x00\x01\x01\x02\x01\x00\x00\x01\x01\x02')
    for w in (1, 2, 3, 4):
        (d0, state0) = audioop.ratecv(datas[w], w, 1, 8000, 16000, None)
        (d, state) = (b'', None)
        for i in range(0, len(datas[w]), w):
            (d1, state) = audioop.ratecv(datas[w][i:i + w], w, 1, 8000, 16000, state)
            d += d1
        self.assertEqual(d, d0)
        self.assertEqual(state, state0)
    expected = {1: packs[1](0, 13, 55, -38, 85, -75, -20), 2: packs[2](0, 3495, 14199, -9776, 22131, -19044, -4762), 3: packs[3](0, 894784, 3635062, -2502602, 5665804, -4875005, -1218752), 4: packs[4](0, 229064922, 930576246, -640665954, 1450446246, -1248001174, -312000294)}
    for w in (1, 2, 3, 4):
        self.assertEqual(audioop.ratecv(datas[w], w, 1, 8000, 8000, None, 3, 1)[0], expected[w])
        self.assertEqual(audioop.ratecv(datas[w], w, 1, 8000, 8000, None, 30, 10)[0], expected[w])
    self.assertRaises(TypeError, audioop.ratecv, b'', 1, 1, 8000, 8000, 42)
    self.assertRaises(TypeError, audioop.ratecv, b'', 1, 1, 8000, 8000, (1, (42,)))
