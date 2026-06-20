# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestSum_test_decimals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    D = Decimal
    data = [D('0.001'), D('5.246'), D('1.702'), D('-0.025'), D('3.974'), D('2.328'), D('4.617'), D('2.843')]
    self.assertEqual(self.func(data), (Decimal, Decimal('20.686'), 8))
