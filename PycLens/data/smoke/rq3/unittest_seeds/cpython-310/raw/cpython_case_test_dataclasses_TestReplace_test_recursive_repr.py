# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestReplace_test_recursive_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class C:
        f: 'C'
    c = C(None)
    c.f = c
    self.assertEqual(repr(c), 'TestReplace.test_recursive_repr.<locals>.C(f=...)')
