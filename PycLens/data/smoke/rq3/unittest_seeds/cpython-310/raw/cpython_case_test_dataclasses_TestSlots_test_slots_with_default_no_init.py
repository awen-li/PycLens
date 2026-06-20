# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestSlots_test_slots_with_default_no_init

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass(slots=True)
    class A:
        a: str
        b: str = field(default='b', init=False)
    obj = A('a')
    self.assertEqual(obj.a, 'a')
    self.assertEqual(obj.b, 'b')
