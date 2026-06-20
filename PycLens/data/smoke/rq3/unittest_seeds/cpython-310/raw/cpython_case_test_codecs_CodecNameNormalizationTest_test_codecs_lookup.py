# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: CodecNameNormalizationTest_test_codecs_lookup

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    FOUND = (1, 2, 3, 4)
    NOT_FOUND = (None, None, None, None)

    def search_function(encoding):
        if encoding == 'aaa_8':
            return FOUND
        else:
            return NOT_FOUND
    codecs.register(search_function)
    self.addCleanup(codecs.unregister, search_function)
    self.assertEqual(FOUND, codecs.lookup('aaa_8'))
    self.assertEqual(FOUND, codecs.lookup('AAA-8'))
    self.assertEqual(FOUND, codecs.lookup('AAA---8'))
    self.assertEqual(FOUND, codecs.lookup('AAA   8'))
    self.assertEqual(FOUND, codecs.lookup('aaaé€-8'))
    self.assertEqual(NOT_FOUND, codecs.lookup('AAA.8'))
    self.assertEqual(NOT_FOUND, codecs.lookup('AAA...8'))
    self.assertEqual(NOT_FOUND, codecs.lookup('BBB-8'))
    self.assertEqual(NOT_FOUND, codecs.lookup('BBB.8'))
    self.assertEqual(NOT_FOUND, codecs.lookup('aé€-8'))
