# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestKeywordArgs_test_KW_ONLY_as_string

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class A:
        a: int
        _: 'dataclasses.KW_ONLY'
        b: int
        c: int
    A(3, c=5, b=4)
    msg = 'takes 2 positional arguments but 4 were given'
    with self.assertRaisesRegex(TypeError, msg):
        A(3, 4, 5)
