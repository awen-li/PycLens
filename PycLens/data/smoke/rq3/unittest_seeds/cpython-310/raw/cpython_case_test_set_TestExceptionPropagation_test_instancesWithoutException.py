# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestExceptionPropagation_test_instancesWithoutException

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    set([1, 2, 3])
    set((1, 2, 3))
    set({'one': 1, 'two': 2, 'three': 3})
    set(range(3))
    set('abc')
    set(gooditer())
