# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_helper_asdict_copy_values

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class C:
        x: int
        y: List[int] = field(default_factory=list)
    initial = []
    c = C(1, initial)
    d = asdict(c)
    self.assertEqual(d['y'], initial)
    self.assertIsNot(d['y'], initial)
    c = C(1)
    d = asdict(c)
    d['y'].append(1)
    self.assertEqual(c.y, [])
