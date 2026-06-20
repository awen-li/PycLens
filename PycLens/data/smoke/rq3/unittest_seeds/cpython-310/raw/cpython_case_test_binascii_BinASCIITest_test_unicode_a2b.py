# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_binascii.py
# case: BinASCIITest_test_unicode_a2b

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    MAX_ALL = 45
    raw = self.rawdata[:MAX_ALL]
    for (fa, fb) in zip(a2b_functions, b2a_functions):
        if fa == 'rledecode_hqx':
            continue
        a2b = getattr(binascii, fa)
        b2a = getattr(binascii, fb)
        try:
            a = b2a(self.type2test(raw))
            binary_res = a2b(a)
            a = a.decode('ascii')
            res = a2b(a)
        except Exception as err:
            self.fail('{}/{} conversion raises {!r}'.format(fb, fa, err))
        if fb == 'b2a_hqx':
            (res, _) = res
            (binary_res, _) = binary_res
        self.assertEqual(res, raw, '{}/{} conversion: {!r} != {!r}'.format(fb, fa, res, raw))
        self.assertEqual(res, binary_res)
        self.assertIsInstance(res, bytes)
        self.assertRaises(ValueError, a2b, '\x80')
