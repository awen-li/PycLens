# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: PunycodeTest_test_encode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (uni, puny) in punycode_testcases:
        self.assertEqual(str(uni.encode('punycode'), 'ascii').lower(), str(puny, 'ascii').lower())
