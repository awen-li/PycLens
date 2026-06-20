# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestFrozen_test_inherit_nonfrozen_from_empty

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class C:
        pass

    @dataclass
    class D(C):
        j: int
    d = D(3)
    self.assertEqual(d.j, 3)
    self.assertIsInstance(d, C)
