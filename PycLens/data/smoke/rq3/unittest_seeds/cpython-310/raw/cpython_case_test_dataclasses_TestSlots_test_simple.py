# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestSlots_test_simple

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class C:
        __slots__ = ('x',)
        x: Any
    with self.assertRaisesRegex(TypeError, "__init__\\(\\) missing 1 required positional argument: 'x'"):
        C()
    c = C(10)
    self.assertEqual(c.x, 10)
    c.x = 5
    self.assertEqual(c.x, 5)
    with self.assertRaisesRegex(AttributeError, "'C' object has no attribute 'y'"):
        c.y = 5
