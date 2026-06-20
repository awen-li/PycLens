# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_post_init_super

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class B:

        def __post_init__(self):
            raise CustomError()

    @dataclass
    class C(B):

        def __post_init__(self):
            self.x = 5
    self.assertEqual(C().x, 5)

    @dataclass
    class C(B):

        def __post_init__(self):
            super().__post_init__()
    with self.assertRaises(CustomError):
        C()

    @dataclass
    class C(B):
        pass
    with self.assertRaises(CustomError):
        C()
