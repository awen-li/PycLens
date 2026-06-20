# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestInit_test_no_init

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass(init=False)
    class C:
        i: int = 0
    self.assertEqual(C().i, 0)

    @dataclass(init=False)
    class C:
        i: int = 2

        def __init__(self):
            self.i = 3
    self.assertEqual(C().i, 3)
