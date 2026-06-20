# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_binascii.py
# case: BinASCIITest_test_returned_value

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    MAX_ALL = 45
    raw = self.rawdata[:MAX_ALL]
    for (fa, fb) in zip(a2b_functions, b2a_functions):
        a2b = getattr(binascii, fa)
        b2a = getattr(binascii, fb)
        try:
            a = b2a(self.type2test(raw))
            res = a2b(self.type2test(a))
        except Exception as err:
            self.fail('{}/{} conversion raises {!r}'.format(fb, fa, err))
        if fb == 'b2a_hqx':
            (res, _) = res
        self.assertEqual(res, raw, '{}/{} conversion: {!r} != {!r}'.format(fb, fa, res, raw))
        self.assertIsInstance(res, bytes)
        self.assertIsInstance(a, bytes)
        self.assertLess(max(a), 128)
    self.assertIsInstance(binascii.crc_hqx(raw, 0), int)
    self.assertIsInstance(binascii.crc32(raw), int)
