# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: TypesTest_test_decode_unicode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    decoders = [codecs.utf_7_decode, codecs.utf_8_decode, codecs.utf_16_le_decode, codecs.utf_16_be_decode, codecs.utf_16_ex_decode, codecs.utf_32_decode, codecs.utf_32_le_decode, codecs.utf_32_be_decode, codecs.utf_32_ex_decode, codecs.latin_1_decode, codecs.ascii_decode, codecs.charmap_decode]
    if hasattr(codecs, 'mbcs_decode'):
        decoders.append(codecs.mbcs_decode)
    for decoder in decoders:
        self.assertRaises(TypeError, decoder, 'xxx')
