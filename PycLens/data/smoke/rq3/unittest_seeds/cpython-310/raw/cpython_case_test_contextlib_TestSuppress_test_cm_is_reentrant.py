# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib.py
# case: TestSuppress_test_cm_is_reentrant

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ignore_exceptions = suppress(Exception)
    with ignore_exceptions:
        pass
    with ignore_exceptions:
        len(5)
    with ignore_exceptions:
        with ignore_exceptions:
            len(5)
        outer_continued = True
        1 / 0
    self.assertTrue(outer_continued)
