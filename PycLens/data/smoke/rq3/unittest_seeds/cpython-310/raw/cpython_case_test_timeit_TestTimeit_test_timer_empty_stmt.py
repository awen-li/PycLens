# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_timeit.py
# case: TestTimeit_test_timer_empty_stmt

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    timeit.Timer(stmt='')
    timeit.Timer(stmt=' \n\t\x0c')
    timeit.Timer(stmt='# comment')
