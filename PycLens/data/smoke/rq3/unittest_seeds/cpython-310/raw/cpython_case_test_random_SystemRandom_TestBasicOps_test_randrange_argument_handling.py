# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: SystemRandom_TestBasicOps_test_randrange_argument_handling

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    randrange = self.gen.randrange
    with self.assertWarns(DeprecationWarning):
        randrange(10.0, 20, 2)
    with self.assertWarns(DeprecationWarning):
        randrange(10, 20.0, 2)
    with self.assertWarns(DeprecationWarning):
        randrange(10, 20, 1.0)
    with self.assertWarns(DeprecationWarning):
        randrange(10, 20, 2.0)
    with self.assertWarns(DeprecationWarning):
        with self.assertRaises(ValueError):
            randrange(10.5)
    with self.assertWarns(DeprecationWarning):
        with self.assertRaises(ValueError):
            randrange(10, 20.5)
    with self.assertWarns(DeprecationWarning):
        with self.assertRaises(ValueError):
            randrange(10, 20, 1.5)
