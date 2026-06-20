# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: MersenneTwister_TestBasicOps_test_bug_31478

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class BadInt(int):

        def __abs__(self):
            return None
    try:
        self.gen.seed(BadInt())
    except TypeError:
        pass
