# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: CodecsModuleTest_test_all

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    api = ('encode', 'decode', 'register', 'CodecInfo', 'Codec', 'IncrementalEncoder', 'IncrementalDecoder', 'StreamReader', 'StreamWriter', 'lookup', 'getencoder', 'getdecoder', 'getincrementalencoder', 'getincrementaldecoder', 'getreader', 'getwriter', 'register_error', 'lookup_error', 'strict_errors', 'replace_errors', 'ignore_errors', 'xmlcharrefreplace_errors', 'backslashreplace_errors', 'namereplace_errors', 'open', 'EncodedFile', 'iterencode', 'iterdecode', 'BOM', 'BOM_BE', 'BOM_LE', 'BOM_UTF8', 'BOM_UTF16', 'BOM_UTF16_BE', 'BOM_UTF16_LE', 'BOM_UTF32', 'BOM_UTF32_BE', 'BOM_UTF32_LE', 'BOM32_BE', 'BOM32_LE', 'BOM64_BE', 'BOM64_LE', 'StreamReaderWriter', 'StreamRecoder')
    self.assertCountEqual(api, codecs.__all__)
    for api in codecs.__all__:
        getattr(codecs, api)
