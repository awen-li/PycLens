# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestMedian_test_odd_decimals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    D = Decimal
    data = [D('2.5'), D('3.1'), D('4.2'), D('5.7'), D('5.8')]
    assert len(data) % 2 == 1
    random.shuffle(data)
    self.assertEqual(self.func(data), D('4.2'))
