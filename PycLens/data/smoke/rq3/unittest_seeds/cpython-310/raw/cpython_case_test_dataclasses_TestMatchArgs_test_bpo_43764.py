# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestMatchArgs_test_bpo_43764

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass(repr=False, eq=False, init=False)
    class X:
        a: int
        b: int
        c: int
    self.assertEqual(X.__match_args__, ('a', 'b', 'c'))
