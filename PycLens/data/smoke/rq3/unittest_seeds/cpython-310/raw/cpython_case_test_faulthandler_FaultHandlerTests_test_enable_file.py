# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_faulthandler.py
# case: FaultHandlerTests_test_enable_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with temporary_filename() as filename:
        self.check_fatal_error("\n                import faulthandler\n                output = open({filename}, 'wb')\n                faulthandler.enable(output)\n                faulthandler._sigsegv()\n                ".format(filename=repr(filename)), 4, 'Segmentation fault', filename=filename)
