# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: MiscellaneousTestCase_test_filter_properties_roundtrip

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    spec1 = lzma._decode_filter_properties(lzma.FILTER_LZMA1, b']\x00\x00\x80\x00')
    reencoded = lzma._encode_filter_properties(spec1)
    spec2 = lzma._decode_filter_properties(lzma.FILTER_LZMA1, reencoded)
    self.assertEqual(spec1, spec2)
