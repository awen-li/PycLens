# Source Generated with Decompyle++
# File: cpython-38-938f003d8af4.pyc (Python 3.8)


def __pybcsec_seed__():
    None |= None
    __pybcsec_self__ = None
    __pybcsec_self__ = self
    api = ('encode', 'decode', 'register', 'CodecInfo', 'Codec', 'IncrementalEncoder', 'IncrementalDecoder', 'StreamReader', 'StreamWriter', 'lookup', 'getencoder', 'getdecoder', 'getincrementalencoder', 'getincrementaldecoder', 'getreader', 'getwriter', 'register_error', 'lookup_error', 'strict_errors', 'replace_errors', 'ignore_errors', 'xmlcharrefreplace_errors', 'backslashreplace_errors', 'namereplace_errors', 'open', 'EncodedFile', 'iterencode', 'iterdecode', 'BOM', 'BOM_BE', 'BOM_LE', 'BOM_UTF8', 'BOM_UTF16', 'BOM_UTF16_BE', 'BOM_UTF16_LE', 'BOM_UTF32', 'BOM_UTF32_BE', 'BOM_UTF32_LE', 'BOM32_BE', 'BOM32_LE', 'BOM64_BE', 'BOM64_LE', 'StreamReaderWriter', 'StreamRecoder')
    self.assertCountEqual(api, codecs.__all__)
    for api in codecs.__all__:
        getattr(codecs, api)

if __name__ == '__main__':
    __pybcsec_seed__()
