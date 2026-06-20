# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_default_missing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Color(Enum):
        RED = 1
        GREEN = 2
        BLUE = 3
    try:
        Color(7)
    except ValueError as exc:
        self.assertTrue(exc.__context__ is None)
    else:
        raise Exception('Exception not raised.')
