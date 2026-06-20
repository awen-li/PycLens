# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_helper_astuple_factory

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class C:
        x: int
        y: int
    NT = namedtuple('NT', 'x y')

    def nt(lst):
        return NT(*lst)
    c = C(1, 2)
    t = astuple(c, tuple_factory=nt)
    self.assertEqual(t, NT(1, 2))
    self.assertIsNot(t, astuple(c, tuple_factory=nt))
    c.x = 42
    t = astuple(c, tuple_factory=nt)
    self.assertEqual(t, NT(42, 2))
    self.assertIs(type(t), NT)
