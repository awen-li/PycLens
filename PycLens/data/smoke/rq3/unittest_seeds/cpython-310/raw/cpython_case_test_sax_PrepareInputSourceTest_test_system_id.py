# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sax.py
# case: PrepareInputSourceTest_test_system_id

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    src = InputSource(self.file)
    prep = prepare_input_source(src)
    self.assertIsNone(prep.getCharacterStream())
    self.checkContent(prep.getByteStream(), b'This was read from a file.')
