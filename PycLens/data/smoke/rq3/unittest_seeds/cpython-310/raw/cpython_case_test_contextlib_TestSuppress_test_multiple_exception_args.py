# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib.py
# case: TestSuppress_test_multiple_exception_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with suppress(ZeroDivisionError, TypeError):
        1 / 0
    with suppress(ZeroDivisionError, TypeError):
        len(5)
