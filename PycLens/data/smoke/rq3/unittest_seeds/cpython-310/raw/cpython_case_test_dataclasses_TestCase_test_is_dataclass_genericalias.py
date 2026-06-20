# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_is_dataclass_genericalias

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class A(types.GenericAlias):
        origin: type
        args: type
    self.assertTrue(is_dataclass(A))
    a = A(list, int)
    self.assertTrue(is_dataclass(type(a)))
    self.assertTrue(is_dataclass(a))
