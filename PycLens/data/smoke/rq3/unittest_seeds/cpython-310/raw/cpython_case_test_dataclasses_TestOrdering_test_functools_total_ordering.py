# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestOrdering_test_functools_total_ordering

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @total_ordering
    @dataclass
    class C:
        x: int

        def __lt__(self, other):
            return self.x >= other
    self.assertLess(C(0), -1)
    self.assertLessEqual(C(0), -1)
    self.assertGreater(C(0), 1)
    self.assertGreaterEqual(C(0), 1)
