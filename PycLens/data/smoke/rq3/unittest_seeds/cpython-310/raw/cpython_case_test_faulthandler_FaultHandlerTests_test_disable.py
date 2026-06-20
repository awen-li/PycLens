# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_faulthandler.py
# case: FaultHandlerTests_test_disable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = '\n            import faulthandler\n            faulthandler.enable()\n            faulthandler.disable()\n            faulthandler._sigsegv()\n            '
    not_expected = 'Fatal Python error'
    (stderr, exitcode) = self.get_output(code)
    stderr = '\n'.join(stderr)
    self.assertTrue(not_expected not in stderr, '%r is present in %r' % (not_expected, stderr))
    self.assertNotEqual(exitcode, 0)
