# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestSlots_test_generated_slots

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass(slots=True)
    class C:
        x: int
        y: int
    c = C(1, 2)
    self.assertEqual((c.x, c.y), (1, 2))
    c.x = 3
    c.y = 4
    self.assertEqual((c.x, c.y), (3, 4))
    with self.assertRaisesRegex(AttributeError, "'C' object has no attribute 'z'"):
        c.z = 5
