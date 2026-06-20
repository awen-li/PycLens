# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_binascii.py
# case: BinASCIITest_test_unicode_b2a

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for func in set(all_functions) - set(a2b_functions) | {'rledecode_hqx'}:
        try:
            self.assertRaises(TypeError, getattr(binascii, func), 'test')
        except Exception as err:
            self.fail('{}("test") raises {!r}'.format(func, err))
    self.assertRaises(TypeError, binascii.crc_hqx, 'test', 0)
