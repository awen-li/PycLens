# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestRepr_test_overwriting_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class C:
        x: int

        def __repr__(self):
            return 'x'
    self.assertEqual(repr(C(0)), 'x')

    @dataclass(repr=True)
    class C:
        x: int

        def __repr__(self):
            return 'x'
    self.assertEqual(repr(C(0)), 'x')

    @dataclass(repr=False)
    class C:
        x: int

        def __repr__(self):
            return 'x'
    self.assertEqual(repr(C(0)), 'x')
