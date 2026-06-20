# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestMean_test_decimals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    D = Decimal
    data = [D('1.634'), D('2.517'), D('3.912'), D('4.072'), D('5.813')]
    random.shuffle(data)
    self.assertEqual(self.func(data), D('3.5896'))
