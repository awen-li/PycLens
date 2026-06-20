# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: ContextAPItests_test_from_legacy_strings

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import _testcapi
    c = self.decimal.Context()
    for rnd in RoundingModes:
        c.rounding = _testcapi.unicode_legacy_string(rnd)
        self.assertEqual(c.rounding, rnd)
    s = _testcapi.unicode_legacy_string('')
    self.assertRaises(TypeError, setattr, c, 'rounding', s)
    s = _testcapi.unicode_legacy_string('ROUND_\x00UP')
    self.assertRaises(TypeError, setattr, c, 'rounding', s)
