# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: TracebackFormatTests_test_recursive_traceback_cpython_internal

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from _testcapi import exception_print

    def render_exc():
        (exc_type, exc_value, exc_tb) = sys.exc_info()
        exception_print(exc_value)
    self._check_recursive_traceback_display(render_exc)
