# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: UnionTests_test_or_type_operator_with_TypeVar

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    TV = typing.TypeVar('T')
    assert TV | str == typing.Union[TV, str]
    assert str | TV == typing.Union[str, TV]
    self.assertIs((int | TV)[int], int)
    self.assertIs((TV | int)[int], int)
