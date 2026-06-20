# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_class_var

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class C:
        x: int
        y: int = 10
        z: ClassVar[int] = 1000
        w: ClassVar[int] = 2000
        t: ClassVar[int] = 3000
        s: ClassVar = 4000
    c = C(5)
    self.assertEqual(repr(c), 'TestCase.test_class_var.<locals>.C(x=5, y=10)')
    self.assertEqual(len(fields(C)), 2)
    self.assertEqual(len(C.__annotations__), 6)
    self.assertEqual(c.z, 1000)
    self.assertEqual(c.w, 2000)
    self.assertEqual(c.t, 3000)
    self.assertEqual(c.s, 4000)
    C.z += 1
    self.assertEqual(c.z, 1001)
    c = C(20)
    self.assertEqual((c.x, c.y), (20, 10))
    self.assertEqual(c.z, 1001)
    self.assertEqual(c.w, 2000)
    self.assertEqual(c.t, 3000)
    self.assertEqual(c.s, 4000)
