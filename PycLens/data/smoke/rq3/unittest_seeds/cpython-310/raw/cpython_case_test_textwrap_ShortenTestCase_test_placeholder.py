# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_textwrap.py
# case: ShortenTestCase_test_placeholder

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    text = "Hello there, how are you this fine day? I'm glad to hear it!"
    self.check_shorten(text, 17, 'Hello there,$$', placeholder='$$')
    self.check_shorten(text, 18, 'Hello there, how$$', placeholder='$$')
    self.check_shorten(text, 18, 'Hello there, $$', placeholder=' $$')
    self.check_shorten(text, len(text), text, placeholder='$$')
    self.check_shorten(text, len(text) - 1, "Hello there, how are you this fine day? I'm glad to hear$$", placeholder='$$')
