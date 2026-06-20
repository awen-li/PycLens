# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: TypedDictTests_test_optional_keys

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Point2Dor3D(Point2D, total=False):
        z: int
    assert Point2Dor3D.__required_keys__ == frozenset(['x', 'y'])
    assert Point2Dor3D.__optional_keys__ == frozenset(['z'])
