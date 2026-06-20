# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_audioop.py
# case: TestAudioop_test_reverse

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for w in (1, 2, 3, 4):
        self.assertEqual(audioop.reverse(b'', w), b'')
        self.assertEqual(audioop.reverse(bytearray(), w), b'')
        self.assertEqual(audioop.reverse(memoryview(b''), w), b'')
        self.assertEqual(audioop.reverse(packs[w](0, 1, 2), w), packs[w](2, 1, 0))
