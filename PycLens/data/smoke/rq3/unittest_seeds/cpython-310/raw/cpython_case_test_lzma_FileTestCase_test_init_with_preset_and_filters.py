# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: FileTestCase_test_init_with_preset_and_filters

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(ValueError):
        LZMAFile(BytesIO(), 'w', format=lzma.FORMAT_RAW, preset=6, filters=FILTERS_RAW_1)
