# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestRepr_test_no_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass(repr=False)
    class C:
        x: int
    self.assertIn(f'{__name__}.TestRepr.test_no_repr.<locals>.C object at', repr(C(3)))

    @dataclass(repr=False)
    class C:
        x: int

        def __repr__(self):
            return 'C-class'
    self.assertEqual(repr(C(3)), 'C-class')
