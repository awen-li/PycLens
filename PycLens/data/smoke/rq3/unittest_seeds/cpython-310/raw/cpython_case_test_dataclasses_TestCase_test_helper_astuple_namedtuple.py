# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_helper_astuple_namedtuple

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = namedtuple('T', 'a b c')

    @dataclass
    class C:
        x: str
        y: T
    c = C('outer', T(1, C('inner', T(11, 12, 13)), 2))
    t = astuple(c)
    self.assertEqual(t, ('outer', T(1, ('inner', (11, 12, 13)), 2)))
    t = astuple(c, tuple_factory=list)
    self.assertEqual(t, ['outer', T(1, ['inner', T(11, 12, 13)], 2)])
