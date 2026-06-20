# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestReplace_test_classvar

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class C:
        x: int
        y: ClassVar[int] = 1000
    c = C(1)
    d = C(2)
    self.assertIs(c.y, d.y)
    self.assertEqual(c.y, 1000)
    with self.assertRaisesRegex(TypeError, "__init__\\(\\) got an unexpected keyword argument 'y'"):
        replace(c, y=30)
    replace(c, x=5)
