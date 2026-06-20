# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestHash_test_0_field_hash

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass(frozen=True)
    class C:
        pass
    self.assertEqual(hash(C()), hash(()))

    @dataclass(unsafe_hash=True)
    class C:
        pass
    self.assertEqual(hash(C()), hash(()))
