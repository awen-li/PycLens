# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestSlots_test_generated_slots_value

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass(slots=True)
    class Base:
        x: int
    self.assertEqual(Base.__slots__, ('x',))

    @dataclass(slots=True)
    class Delivered(Base):
        y: int
    self.assertEqual(Delivered.__slots__, ('x', 'y'))

    @dataclass
    class AnotherDelivered(Base):
        z: int
    self.assertTrue('__slots__' not in AnotherDelivered.__dict__)
