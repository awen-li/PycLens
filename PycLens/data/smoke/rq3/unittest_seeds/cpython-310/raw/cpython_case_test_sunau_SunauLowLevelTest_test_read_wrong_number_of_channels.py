# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sunau.py
# case: SunauLowLevelTest_test_read_wrong_number_of_channels

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = struct.pack('>LLLLLL', sunau.AUDIO_FILE_MAGIC, 24, 0, sunau.AUDIO_FILE_ENCODING_LINEAR_8, 11025, 0)
    with self.assertRaisesRegex(sunau.Error, 'bad # of channels'):
        sunau.open(io.BytesIO(b))
