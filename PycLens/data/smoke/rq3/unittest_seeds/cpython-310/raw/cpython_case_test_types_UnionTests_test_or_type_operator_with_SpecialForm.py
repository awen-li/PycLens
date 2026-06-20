# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: UnionTests_test_or_type_operator_with_SpecialForm

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    assert typing.Any | str == typing.Union[typing.Any, str]
    assert typing.NoReturn | str == typing.Union[typing.NoReturn, str]
    assert typing.Optional[int] | str == typing.Union[typing.Optional[int], str]
    assert typing.Optional[int] | str == typing.Union[int, str, None]
    assert typing.Union[int, bool] | str == typing.Union[int, bool, str]
