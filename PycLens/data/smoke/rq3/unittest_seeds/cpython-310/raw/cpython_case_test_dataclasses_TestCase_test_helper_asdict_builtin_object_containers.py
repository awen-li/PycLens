# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_helper_asdict_builtin_object_containers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class Child:
        d: object

    @dataclass
    class Parent:
        child: Child
    self.assertEqual(asdict(Parent(Child([1]))), {'child': {'d': [1]}})
    self.assertEqual(asdict(Parent(Child({1: 2}))), {'child': {'d': {1: 2}}})
