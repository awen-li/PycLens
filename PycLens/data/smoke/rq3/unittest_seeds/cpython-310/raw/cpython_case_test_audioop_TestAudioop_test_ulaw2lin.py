# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_audioop.py
# case: TestAudioop_test_ulaw2lin

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    encoded = b'\x00\x0e(?Wjv|~\x7f\x80\x8e\xa8\xbf\xd7\xea\xf6\xfc\xfe\xff'
    src = [-8031, -4447, -1471, -495, -163, -53, -18, -6, -2, 0, 8031, 4447, 1471, 495, 163, 53, 18, 6, 2, 0]
    for w in (1, 2, 3, 4):
        decoded = packs[w](*(x << w * 8 >> 14 for x in src))
        self.assertEqual(audioop.ulaw2lin(encoded, w), decoded)
        self.assertEqual(audioop.ulaw2lin(bytearray(encoded), w), decoded)
        self.assertEqual(audioop.ulaw2lin(memoryview(encoded), w), decoded)
    encoded = bytes(range(127)) + bytes(range(128, 256))
    for w in (2, 3, 4):
        decoded = audioop.ulaw2lin(encoded, w)
        self.assertEqual(audioop.lin2ulaw(decoded, w), encoded)
