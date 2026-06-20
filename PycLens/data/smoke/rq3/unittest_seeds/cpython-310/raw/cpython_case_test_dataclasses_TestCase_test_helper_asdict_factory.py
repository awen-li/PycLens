# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_helper_asdict_factory

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class C:
        x: int
        y: int
    c = C(1, 2)
    d = asdict(c, dict_factory=OrderedDict)
    self.assertEqual(d, OrderedDict([('x', 1), ('y', 2)]))
    self.assertIsNot(d, asdict(c, dict_factory=OrderedDict))
    c.x = 42
    d = asdict(c, dict_factory=OrderedDict)
    self.assertEqual(d, OrderedDict([('x', 42), ('y', 2)]))
    self.assertIs(type(d), OrderedDict)
