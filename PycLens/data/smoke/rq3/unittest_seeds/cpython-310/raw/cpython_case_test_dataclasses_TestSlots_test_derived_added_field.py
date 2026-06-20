# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestSlots_test_derived_added_field

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class Base:
        __slots__ = ('x',)
        x: Any

    @dataclass
    class Derived(Base):
        x: int
        y: int
    d = Derived(1, 2)
    self.assertEqual((d.x, d.y), (1, 2))
    d.z = 10
