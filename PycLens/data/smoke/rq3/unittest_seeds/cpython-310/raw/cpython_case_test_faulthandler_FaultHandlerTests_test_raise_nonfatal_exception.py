# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_faulthandler.py
# case: FaultHandlerTests_test_raise_nonfatal_exception

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for exc in (0, 878082192, 1073741824, 1073745920, 1879048192, 2147483647):
        (output, exitcode) = self.get_output(f'\n                import faulthandler\n                faulthandler.enable()\n                faulthandler._raise_exception(0x{exc:x})\n                ')
        self.assertEqual(output, [])
        self.assertIn(exitcode, (exc, exc & ~268435456))
