# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sax.py
# case: PrepareInputSourceTest_test_character_stream

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    src = InputSource(self.file)
    src.setCharacterStream(self.make_character_stream())
    prep = prepare_input_source(src)
    self.assertIsNone(prep.getByteStream())
    self.checkContent(prep.getCharacterStream(), 'This is a character stream.')
