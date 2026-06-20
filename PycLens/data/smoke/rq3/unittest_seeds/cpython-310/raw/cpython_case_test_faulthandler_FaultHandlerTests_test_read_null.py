# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_faulthandler.py
# case: FaultHandlerTests_test_read_null

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if not MS_WINDOWS:
        self.check_fatal_error('\n                import faulthandler\n                faulthandler.enable()\n                faulthandler._read_null()\n                ', 3, '(?:Segmentation fault|Bus error|Illegal instruction)')
    else:
        self.check_windows_exception('\n                import faulthandler\n                faulthandler.enable()\n                faulthandler._read_null()\n                ', 3, 'access violation')
