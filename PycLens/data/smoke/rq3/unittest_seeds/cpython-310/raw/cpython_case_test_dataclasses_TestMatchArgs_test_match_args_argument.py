# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestMatchArgs_test_match_args_argument

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass(match_args=False)
    class X:
        a: int
    self.assertNotIn('__match_args__', X.__dict__)

    @dataclass(match_args=False)
    class Y:
        a: int
        __match_args__ = ('b',)
    self.assertEqual(Y.__match_args__, ('b',))

    @dataclass(match_args=False)
    class Z(Y):
        z: int
    self.assertEqual(Z.__match_args__, ('b',))

    @dataclass
    class A:
        a: int
        z: int

    @dataclass(match_args=False)
    class B(A):
        b: int
    self.assertEqual(B.__match_args__, ('a', 'z'))
