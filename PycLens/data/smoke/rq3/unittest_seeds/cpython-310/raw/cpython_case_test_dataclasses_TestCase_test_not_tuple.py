# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_not_tuple

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class Point:
        x: int
        y: int
    self.assertNotEqual(Point(1, 2), (1, 2))

    @dataclass
    class C:
        x: int
        y: int
    self.assertNotEqual(Point(1, 3), C(1, 3))
