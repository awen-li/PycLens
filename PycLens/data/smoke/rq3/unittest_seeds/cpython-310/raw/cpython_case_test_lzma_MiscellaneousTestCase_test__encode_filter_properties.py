# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: MiscellaneousTestCase_test__encode_filter_properties

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError):
        lzma._encode_filter_properties(b'not a dict')
    with self.assertRaises(ValueError):
        lzma._encode_filter_properties({'id': 256})
    with self.assertRaises(ValueError):
        lzma._encode_filter_properties({'id': lzma.FILTER_LZMA2, 'junk': 12})
    with self.assertRaises(lzma.LZMAError):
        lzma._encode_filter_properties({'id': lzma.FILTER_DELTA, 'dist': 9001})
    props = lzma._encode_filter_properties({'id': lzma.FILTER_LZMA1, 'pb': 2, 'lp': 0, 'lc': 3, 'dict_size': 8 << 20})
    self.assertEqual(props, b']\x00\x00\x80\x00')
