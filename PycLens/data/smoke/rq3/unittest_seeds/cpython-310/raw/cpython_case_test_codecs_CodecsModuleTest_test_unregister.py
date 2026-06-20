# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: CodecsModuleTest_test_unregister

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    name = 'nonexistent_codec_name'
    search_function = mock.Mock()
    codecs.register(search_function)
    self.assertRaises(TypeError, codecs.lookup, name)
    search_function.assert_called_with(name)
    search_function.reset_mock()
    codecs.unregister(search_function)
    self.assertRaises(LookupError, codecs.lookup, name)
    search_function.assert_not_called()
