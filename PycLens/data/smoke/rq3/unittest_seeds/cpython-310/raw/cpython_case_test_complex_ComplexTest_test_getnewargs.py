# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_complex.py
# case: ComplexTest_test_getnewargs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual((1 + 2j).__getnewargs__(), (1.0, 2.0))
    self.assertEqual((1 - 2j).__getnewargs__(), (1.0, -2.0))
    self.assertEqual(2j.__getnewargs__(), (0.0, 2.0))
    self.assertEqual((-0j).__getnewargs__(), (0.0, -0.0))
    self.assertEqual(complex(0, INF).__getnewargs__(), (0.0, INF))
    self.assertEqual(complex(INF, 0).__getnewargs__(), (INF, 0.0))
