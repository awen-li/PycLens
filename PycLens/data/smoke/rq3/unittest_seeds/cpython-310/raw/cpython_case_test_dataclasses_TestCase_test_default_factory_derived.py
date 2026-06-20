# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_default_factory_derived

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class Foo:
        x: dict = field(default_factory=dict)

    @dataclass
    class Bar(Foo):
        y: int = 1
    self.assertEqual(Foo().x, {})
    self.assertEqual(Bar().x, {})
    self.assertEqual(Bar().y, 1)

    @dataclass
    class Baz(Foo):
        pass
    self.assertEqual(Baz().x, {})
