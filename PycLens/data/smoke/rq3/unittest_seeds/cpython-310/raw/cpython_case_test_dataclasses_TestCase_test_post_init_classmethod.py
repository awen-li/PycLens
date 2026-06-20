# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_post_init_classmethod

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class C:
        flag = False
        x: int
        y: int

        @classmethod
        def __post_init__(cls):
            cls.flag = True
    self.assertFalse(C.flag)
    c = C(3, 4)
    self.assertEqual((c.x, c.y), (3, 4))
    self.assertTrue(C.flag)
