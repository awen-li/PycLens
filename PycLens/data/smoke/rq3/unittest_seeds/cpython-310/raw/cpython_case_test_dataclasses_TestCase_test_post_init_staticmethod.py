# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_post_init_staticmethod

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    flag = False

    @dataclass
    class C:
        x: int
        y: int

        @staticmethod
        def __post_init__():
            nonlocal flag
            flag = True
    self.assertFalse(flag)
    c = C(3, 4)
    self.assertEqual((c.x, c.y), (3, 4))
    self.assertTrue(flag)
