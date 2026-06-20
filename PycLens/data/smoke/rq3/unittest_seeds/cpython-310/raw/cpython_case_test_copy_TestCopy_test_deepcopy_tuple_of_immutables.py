# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_copy.py
# case: TestCopy_test_deepcopy_tuple_of_immutables

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = ((1, 2), 3)
    y = copy.deepcopy(x)
    self.assertIs(x, y)
