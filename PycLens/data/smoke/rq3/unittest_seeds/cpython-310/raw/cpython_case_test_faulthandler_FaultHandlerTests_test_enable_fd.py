# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_faulthandler.py
# case: FaultHandlerTests_test_enable_fd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with tempfile.TemporaryFile('wb+') as fp:
        fd = fp.fileno()
        self.check_fatal_error('\n                import faulthandler\n                import sys\n                faulthandler.enable(%s)\n                faulthandler._sigsegv()\n                ' % fd, 4, 'Segmentation fault', fd=fd)
