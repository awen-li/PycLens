# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sunau.py
# case: SunauLowLevelTest_test_read_too_small_header

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = struct.pack('>LLLLL', sunau.AUDIO_FILE_MAGIC, 20, 0, sunau.AUDIO_FILE_ENCODING_LINEAR_8, 11025)
    with self.assertRaisesRegex(sunau.Error, 'header size too small'):
        sunau.open(io.BytesIO(b))
