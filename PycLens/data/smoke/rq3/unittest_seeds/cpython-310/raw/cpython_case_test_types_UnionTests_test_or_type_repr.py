# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: UnionTests_test_or_type_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    assert repr(int | str) == 'int | str'
    assert repr(int | str | list) == 'int | str | list'
    assert repr(int | (str | list)) == 'int | str | list'
    assert repr(int | None) == 'int | None'
    assert repr(int | type(None)) == 'int | None'
    assert repr(int | typing.GenericAlias(list, int)) == 'int | list[int]'
