# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: TestBasicOps_test_seedargs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MySeed(object):

        def __hash__(self):
            return -1729
    for arg in [None, 0, 1, -1, 10 ** 20, -10 ** 20, False, True, 3.14, 'a']:
        self.gen.seed(arg)
    for arg in [1 + 2j, tuple('abc'), MySeed()]:
        with self.assertWarns(DeprecationWarning):
            self.gen.seed(arg)
    for arg in [list(range(3)), dict(one=1)]:
        with self.assertWarns(DeprecationWarning):
            self.assertRaises(TypeError, self.gen.seed, arg)
    self.assertRaises(TypeError, self.gen.seed, 1, 2, 3, 4)
    self.assertRaises(TypeError, type(self.gen), [])
