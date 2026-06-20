# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestMedianGrouped_test_odd_decimals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    D = Decimal
    data = [D('5.5'), D('6.5'), D('6.5'), D('7.5'), D('8.5')]
    assert len(data) % 2 == 1
    random.shuffle(data)
    self.assertEqual(self.func(data), 6.75)
