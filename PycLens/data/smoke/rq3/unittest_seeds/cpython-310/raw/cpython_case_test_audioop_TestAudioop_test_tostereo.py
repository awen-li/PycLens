# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_audioop.py
# case: TestAudioop_test_tostereo

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for w in (1, 2, 3, 4):
        data1 = datas[w]
        data2 = bytearray(2 * len(data1))
        for k in range(w):
            data2[k::2 * w] = data1[k::w]
        self.assertEqual(audioop.tostereo(data1, w, 1, 0), data2)
        self.assertEqual(audioop.tostereo(data1, w, 0, 0), b'\x00' * len(data2))
        for k in range(w):
            data2[k + w::2 * w] = data1[k::w]
        self.assertEqual(audioop.tostereo(data1, w, 1, 1), data2)
        self.assertEqual(audioop.tostereo(bytearray(data1), w, 1, 1), data2)
        self.assertEqual(audioop.tostereo(memoryview(data1), w, 1, 1), data2)
