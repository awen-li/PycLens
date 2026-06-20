# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestReplace_test_recursive_repr_indirection

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class C:
        f: 'D'

    @dataclass
    class D:
        f: 'C'
    c = C(None)
    d = D(None)
    c.f = d
    d.f = c
    self.assertEqual(repr(c), 'TestReplace.test_recursive_repr_indirection.<locals>.C(f=TestReplace.test_recursive_repr_indirection.<locals>.D(f=...))')
