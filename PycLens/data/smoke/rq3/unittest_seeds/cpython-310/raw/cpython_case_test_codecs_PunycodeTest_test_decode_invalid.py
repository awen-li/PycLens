# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: PunycodeTest_test_decode_invalid

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    testcases = [(b'xn--w&', 'strict', UnicodeError()), (b'xn--w&', 'ignore', 'xn-')]
    for (puny, errors, expected) in testcases:
        with self.subTest(puny=puny, errors=errors):
            if isinstance(expected, Exception):
                self.assertRaises(UnicodeError, puny.decode, 'punycode', errors)
            else:
                self.assertEqual(puny.decode('punycode', errors), expected)
