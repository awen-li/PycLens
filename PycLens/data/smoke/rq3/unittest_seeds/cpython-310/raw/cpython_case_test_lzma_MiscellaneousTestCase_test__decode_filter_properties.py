# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: MiscellaneousTestCase_test__decode_filter_properties

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError):
        lzma._decode_filter_properties(lzma.FILTER_X86, {'should be': bytes})
    with self.assertRaises(lzma.LZMAError):
        lzma._decode_filter_properties(lzma.FILTER_DELTA, b'too long')
    filterspec = lzma._decode_filter_properties(lzma.FILTER_LZMA1, b']\x00\x00\x80\x00')
    self.assertEqual(filterspec['id'], lzma.FILTER_LZMA1)
    self.assertEqual(filterspec['pb'], 2)
    self.assertEqual(filterspec['lp'], 0)
    self.assertEqual(filterspec['lc'], 3)
    self.assertEqual(filterspec['dict_size'], 8 << 20)
