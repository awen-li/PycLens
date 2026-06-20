# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestInit_test_base_has_init

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class B:

        def __init__(self):
            self.z = 100
            pass

    @dataclass
    class C(B):
        x: int = 0
    c = C(10)
    self.assertEqual(c.x, 10)
    self.assertNotIn('z', vars(c))

    @dataclass(init=False)
    class C(B):
        x: int = 10
    c = C()
    self.assertEqual(c.x, 10)
    self.assertEqual(c.z, 100)
