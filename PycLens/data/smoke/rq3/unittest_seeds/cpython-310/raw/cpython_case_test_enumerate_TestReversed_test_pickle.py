# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enumerate.py
# case: TestReversed_test_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for data in ('abc', range(5), tuple(enumerate('abc')), range(1, 17, 5)):
        self.check_pickle(reversed(data), list(data)[::-1])
