# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_helper_asdict_builtin_containers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class User:
        name: str
        id: int

    @dataclass
    class GroupList:
        id: int
        users: List[User]

    @dataclass
    class GroupTuple:
        id: int
        users: Tuple[User, ...]

    @dataclass
    class GroupDict:
        id: int
        users: Dict[str, User]
    a = User('Alice', 1)
    b = User('Bob', 2)
    gl = GroupList(0, [a, b])
    gt = GroupTuple(0, (a, b))
    gd = GroupDict(0, {'first': a, 'second': b})
    self.assertEqual(asdict(gl), {'id': 0, 'users': [{'name': 'Alice', 'id': 1}, {'name': 'Bob', 'id': 2}]})
    self.assertEqual(asdict(gt), {'id': 0, 'users': ({'name': 'Alice', 'id': 1}, {'name': 'Bob', 'id': 2})})
    self.assertEqual(asdict(gd), {'id': 0, 'users': {'first': {'name': 'Alice', 'id': 1}, 'second': {'name': 'Bob', 'id': 2}}})
