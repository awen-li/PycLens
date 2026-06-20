# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_faulthandler.py
# case: FaultHandlerTests_test_ignore_exception

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for exc_code in (3765269347, 3762504530):
        code = f'\n                    import faulthandler\n                    faulthandler.enable()\n                    faulthandler._raise_exception({exc_code})\n                    '
        code = dedent(code)
        (output, exitcode) = self.get_output(code)
        self.assertEqual(output, [])
        self.assertEqual(exitcode, exc_code)
