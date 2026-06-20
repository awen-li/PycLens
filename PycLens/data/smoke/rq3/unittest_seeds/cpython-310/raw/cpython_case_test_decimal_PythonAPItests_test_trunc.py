# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: PythonAPItests_test_trunc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    for x in range(-250, 250):
        s = '%0.2f' % (x / 100.0)
        self.assertEqual(int(Decimal(s)), int(float(s)))
        d = Decimal(s)
        r = d.to_integral(ROUND_DOWN)
        self.assertEqual(Decimal(math.trunc(d)), r)
