# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: TypedDictTests_test_is_typeddict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    assert is_typeddict(Point2D) is True
    assert is_typeddict(Union[str, int]) is False
    assert is_typeddict(Point2D()) is False
