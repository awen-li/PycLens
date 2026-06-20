# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_helper_astuple

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class C:
        x: int
        y: int = 0
    c = C(1)
    self.assertEqual(astuple(c), (1, 0))
    self.assertEqual(astuple(c), astuple(c))
    self.assertIsNot(astuple(c), astuple(c))
    c.y = 42
    self.assertEqual(astuple(c), (1, 42))
    self.assertIs(type(astuple(c)), tuple)
