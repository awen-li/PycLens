# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_helper_asdict_namedtuple

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = namedtuple('T', 'a b c')

    @dataclass
    class C:
        x: str
        y: T
    c = C('outer', T(1, C('inner', T(11, 12, 13)), 2))
    d = asdict(c)
    self.assertEqual(d, {'x': 'outer', 'y': T(1, {'x': 'inner', 'y': T(11, 12, 13)}, 2)})
    d = asdict(c, dict_factory=OrderedDict)
    self.assertEqual(d, {'x': 'outer', 'y': T(1, {'x': 'inner', 'y': T(11, 12, 13)}, 2)})
    self.assertIs(type(d), OrderedDict)
    self.assertIs(type(d['y'][1]), OrderedDict)
