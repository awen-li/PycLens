# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_not_in_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class C:
        x: int = field(repr=False)
    with self.assertRaises(TypeError):
        C()
    c = C(10)
    self.assertEqual(repr(c), 'TestCase.test_not_in_repr.<locals>.C()')

    @dataclass
    class C:
        x: int = field(repr=False)
        y: int
    c = C(10, 20)
    self.assertEqual(repr(c), 'TestCase.test_not_in_repr.<locals>.C(y=20)')
