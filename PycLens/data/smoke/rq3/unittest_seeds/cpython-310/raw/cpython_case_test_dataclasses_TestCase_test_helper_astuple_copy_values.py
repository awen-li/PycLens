# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_helper_astuple_copy_values

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class C:
        x: int
        y: List[int] = field(default_factory=list)
    initial = []
    c = C(1, initial)
    t = astuple(c)
    self.assertEqual(t[1], initial)
    self.assertIsNot(t[1], initial)
    c = C(1)
    t = astuple(c)
    t[1].append(1)
    self.assertEqual(c.y, [])
