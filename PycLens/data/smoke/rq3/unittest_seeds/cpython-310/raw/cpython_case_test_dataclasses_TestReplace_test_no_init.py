# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestReplace_test_no_init

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class C:
        x: int
        y: int = field(init=False, default=10)
    c = C(1)
    c.y = 20
    c1 = replace(c, x=5)
    self.assertEqual((c1.x, c1.y), (5, 10))
    with self.assertRaisesRegex(ValueError, 'init=False'):
        replace(c, x=2, y=30)
    with self.assertRaisesRegex(ValueError, 'init=False'):
        replace(c, y=30)
