# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sax.py
# case: PrepareInputSourceTest_test_text_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    prep = prepare_input_source(self.make_character_stream())
    self.assertIsNone(prep.getByteStream())
    self.checkContent(prep.getCharacterStream(), 'This is a character stream.')
