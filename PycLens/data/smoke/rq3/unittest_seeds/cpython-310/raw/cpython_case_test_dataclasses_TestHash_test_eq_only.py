# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestHash_test_eq_only

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class C:
        i: int

        def __eq__(self, other):
            return self.i == other.i
    self.assertEqual(C(1), C(1))
    self.assertNotEqual(C(1), C(4))

    @dataclass(unsafe_hash=True)
    class C:
        i: int

        def __eq__(self, other):
            return self.i == other.i
    self.assertEqual(C(1), C(1.0))
    self.assertEqual(hash(C(1)), hash(C(1.0)))

    @dataclass(unsafe_hash=True, eq=True)
    class C:
        i: int

        def __eq__(self, other):
            return self.i == 3 and self.i == other.i
    self.assertEqual(C(3), C(3))
    self.assertNotEqual(C(1), C(1))
    self.assertEqual(hash(C(1)), hash(C(1.0)))
