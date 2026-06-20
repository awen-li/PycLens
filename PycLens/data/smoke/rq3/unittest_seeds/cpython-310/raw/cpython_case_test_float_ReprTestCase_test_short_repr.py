# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_float.py
# case: ReprTestCase_test_short_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    test_strings = ['0.0', '1.0', '0.01', '0.02', '0.03', '0.04', '0.05', '1.23456789', '10.0', '100.0', '1000000000000000.0', '9999999999999990.0', '1e+16', '1e+17', '0.001', '0.001001', '0.00010000000000001', '0.0001', '9.999999999999e-05', '1e-05', '8.72293771110361e+25', '7.47005307342313e+26', '2.86438000439698e+28', '8.89142905246179e+28', '3.08578087079232e+35']
    for s in test_strings:
        negs = '-' + s
        self.assertEqual(s, repr(float(s)))
        self.assertEqual(negs, repr(float(negs)))
        self.assertEqual(repr(float(s)), str(float(s)))
        self.assertEqual(repr(float(negs)), str(float(negs)))
