# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sunau.py
# case: SunauLowLevelTest_test_read_wrong_encoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = struct.pack('>LLLLLL', sunau.AUDIO_FILE_MAGIC, 24, 0, 0, 11025, 1)
    with self.assertRaisesRegex(sunau.Error, 'encoding not \\(yet\\) supported'):
        sunau.open(io.BytesIO(b))
