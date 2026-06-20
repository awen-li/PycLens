# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_overwrite_fields_in_derived_class

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class Base:
        x: Any = 15.0
        y: int = 0

    @dataclass
    class C1(Base):
        z: int = 10
        x: int = 15
    o = Base()
    self.assertEqual(repr(o), 'TestCase.test_overwrite_fields_in_derived_class.<locals>.Base(x=15.0, y=0)')
    o = C1()
    self.assertEqual(repr(o), 'TestCase.test_overwrite_fields_in_derived_class.<locals>.C1(x=15, y=0, z=10)')
    o = C1(x=5)
    self.assertEqual(repr(o), 'TestCase.test_overwrite_fields_in_derived_class.<locals>.C1(x=5, y=0, z=10)')
