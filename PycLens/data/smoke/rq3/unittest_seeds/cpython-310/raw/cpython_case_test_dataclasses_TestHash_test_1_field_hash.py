# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestHash_test_1_field_hash

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass(frozen=True)
    class C:
        x: int
    self.assertEqual(hash(C(4)), hash((4,)))
    self.assertEqual(hash(C(42)), hash((42,)))

    @dataclass(unsafe_hash=True)
    class C:
        x: int
    self.assertEqual(hash(C(4)), hash((4,)))
    self.assertEqual(hash(C(42)), hash((42,)))
