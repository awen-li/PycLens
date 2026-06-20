# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_audioop.py
# case: TestAudioop_test_alaw2lin

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    encoded = b'\x00\x03$*QTUXkq\x7f\x80\x83\xa4\xaa\xd1\xd4\xd5\xd8\xeb\xf1\xff'
    src = [-688, -720, -2240, -4032, -9, -3, -1, -27, -244, -82, -106, 688, 720, 2240, 4032, 9, 3, 1, 27, 244, 82, 106]
    for w in (1, 2, 3, 4):
        decoded = packs[w](*(x << w * 8 >> 13 for x in src))
        self.assertEqual(audioop.alaw2lin(encoded, w), decoded)
        self.assertEqual(audioop.alaw2lin(bytearray(encoded), w), decoded)
        self.assertEqual(audioop.alaw2lin(memoryview(encoded), w), decoded)
    encoded = bytes(range(256))
    for w in (2, 3, 4):
        decoded = audioop.alaw2lin(encoded, w)
        self.assertEqual(audioop.lin2alaw(decoded, w), encoded)
