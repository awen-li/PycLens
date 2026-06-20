# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestHarmonicMean_test_decimals_exact

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    D = Decimal
    self.assertEqual(self.func([D(15), D(30), D(60), D(60)]), D(30))
    data = [D('0.05'), D('0.10'), D('0.20'), D('0.20')]
    random.shuffle(data)
    self.assertEqual(self.func(data), D('0.10'))
    data = [D('1.68'), D('0.32'), D('5.94'), D('2.75')]
    random.shuffle(data)
    self.assertEqual(self.func(data), D(66528) / 70723)
