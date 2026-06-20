# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_helper_asdict_nested

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class UserId:
        token: int
        group: int

    @dataclass
    class User:
        name: str
        id: UserId
    u = User('Joe', UserId(123, 1))
    d = asdict(u)
    self.assertEqual(d, {'name': 'Joe', 'id': {'token': 123, 'group': 1}})
    self.assertIsNot(asdict(u), asdict(u))
    u.id.group = 2
    self.assertEqual(asdict(u), {'name': 'Joe', 'id': {'token': 123, 'group': 2}})
