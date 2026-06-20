# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestReplace_test_recursive_repr_indirection_two

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class C:
        f: 'D'

    @dataclass
    class D:
        f: 'E'

    @dataclass
    class E:
        f: 'C'
    c = C(None)
    d = D(None)
    e = E(None)
    c.f = d
    d.f = e
    e.f = c
    self.assertEqual(repr(c), 'TestReplace.test_recursive_repr_indirection_two.<locals>.C(f=TestReplace.test_recursive_repr_indirection_two.<locals>.D(f=TestReplace.test_recursive_repr_indirection_two.<locals>.E(f=...)))')
