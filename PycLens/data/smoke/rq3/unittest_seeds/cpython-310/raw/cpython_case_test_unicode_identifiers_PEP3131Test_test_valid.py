# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode_identifiers.py
# case: PEP3131Test_test_valid

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class T:
        ä = 1
        μ = 2
        蟒 = 3
        x󠄀 = 4
    self.assertEqual(getattr(T, 'ä'), 1)
    self.assertEqual(getattr(T, 'μ'), 2)
    self.assertEqual(getattr(T, '蟒'), 3)
    self.assertEqual(getattr(T, 'x󠄀'), 4)
