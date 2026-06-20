# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestHash_test_unsafe_hash

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass(unsafe_hash=True)
    class C:
        x: int
        y: str
    self.assertEqual(hash(C(1, 'foo')), hash((1, 'foo')))
