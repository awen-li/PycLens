# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xxlimited.py
# case: TestXXLimited35_test_xxo_demo

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    xxo = self.module.Xxo()
    other = self.module.Xxo()
    self.assertEqual(xxo.demo('abc'), 'abc')
    self.assertEqual(xxo.demo(0), None)
