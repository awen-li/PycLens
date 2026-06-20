# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_format.py
# case: FormatTest_test_precision

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = 1.2
    self.assertEqual(format(f, '.0f'), '1')
    self.assertEqual(format(f, '.3f'), '1.200')
    with self.assertRaises(ValueError) as cm:
        format(f, '.%sf' % (sys.maxsize + 1))
    c = complex(f)
    self.assertEqual(format(c, '.0f'), '1+0j')
    self.assertEqual(format(c, '.3f'), '1.200+0.000j')
    with self.assertRaises(ValueError) as cm:
        format(c, '.%sf' % (sys.maxsize + 1))
