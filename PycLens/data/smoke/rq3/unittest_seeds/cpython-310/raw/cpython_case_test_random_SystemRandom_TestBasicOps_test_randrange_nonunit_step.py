# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: SystemRandom_TestBasicOps_test_randrange_nonunit_step

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    rint = self.gen.randrange(0, 10, 2)
    self.assertIn(rint, (0, 2, 4, 6, 8))
    rint = self.gen.randrange(0, 2, 2)
    self.assertEqual(rint, 0)
