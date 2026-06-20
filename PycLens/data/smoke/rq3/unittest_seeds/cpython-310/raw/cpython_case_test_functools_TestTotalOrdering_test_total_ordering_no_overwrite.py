# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestTotalOrdering_test_total_ordering_no_overwrite

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @functools.total_ordering
    class A(int):
        pass
    self.assertTrue(A(1) < A(2))
    self.assertTrue(A(2) > A(1))
    self.assertTrue(A(1) <= A(2))
    self.assertTrue(A(2) >= A(1))
    self.assertTrue(A(2) <= A(2))
    self.assertTrue(A(2) >= A(2))
