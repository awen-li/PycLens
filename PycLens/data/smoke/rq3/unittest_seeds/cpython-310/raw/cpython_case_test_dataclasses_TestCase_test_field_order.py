# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_field_order

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class B:
        a: str = 'B:a'
        b: str = 'B:b'
        c: str = 'B:c'

    @dataclass
    class C(B):
        b: str = 'C:b'
    self.assertEqual([(f.name, f.default) for f in fields(C)], [('a', 'B:a'), ('b', 'C:b'), ('c', 'B:c')])

    @dataclass
    class D(B):
        c: str = 'D:c'
    self.assertEqual([(f.name, f.default) for f in fields(D)], [('a', 'B:a'), ('b', 'B:b'), ('c', 'D:c')])

    @dataclass
    class E(D):
        a: str = 'E:a'
        d: str = 'E:d'
    self.assertEqual([(f.name, f.default) for f in fields(E)], [('a', 'E:a'), ('b', 'B:b'), ('c', 'D:c'), ('d', 'E:d')])
