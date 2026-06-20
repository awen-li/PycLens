# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_faulthandler.py
# case: FaultHandlerTests_test_raise_exception

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (exc, name) in (('EXCEPTION_ACCESS_VIOLATION', 'access violation'), ('EXCEPTION_INT_DIVIDE_BY_ZERO', 'int divide by zero'), ('EXCEPTION_STACK_OVERFLOW', 'stack overflow')):
        self.check_windows_exception(f'\n                import faulthandler\n                faulthandler.enable()\n                faulthandler._raise_exception(faulthandler._{exc})\n                ', 3, name)
