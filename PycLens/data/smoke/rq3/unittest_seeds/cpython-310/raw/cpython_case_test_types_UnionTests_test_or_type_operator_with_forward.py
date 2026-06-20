# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: UnionTests_test_or_type_operator_with_forward

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = typing.TypeVar('T')
    ForwardAfter = T | 'Forward'
    ForwardBefore = 'Forward' | T

    def forward_after(x: ForwardAfter[int]) -> None:
        ...

    def forward_before(x: ForwardBefore[int]) -> None:
        ...
    assert typing.get_args(typing.get_type_hints(forward_after)['x']) == (int, Forward)
    assert typing.get_args(typing.get_type_hints(forward_before)['x']) == (int, Forward)
