# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sax.py
# case: PrepareInputSourceTest_test_path_objects

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    prep = prepare_input_source(FakePath(self.file))
    self.assertIsNone(prep.getCharacterStream())
    self.checkContent(prep.getByteStream(), b'This was read from a file.')
