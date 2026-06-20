# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestMedianLow_test_even_decimals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    D = Decimal
    data = [D('1.1'), D('2.2'), D('3.3'), D('4.4'), D('5.5'), D('6.6')]
    assert len(data) % 2 == 0
    random.shuffle(data)
    self.assertEqual(self.func(data), D('3.3'))
