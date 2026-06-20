# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: UnionTests_test_or_type_operator_with_TypedDict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Point2D(typing.TypedDict):
        x: int
        y: int
        label: str
    assert Point2D | str == typing.Union[Point2D, str]
