# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: CodecsModuleTest_test_getencoder

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, codecs.getencoder)
    self.assertRaises(LookupError, codecs.getencoder, '__spam__')
