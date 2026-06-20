# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_faulthandler.py
# case: FaultHandlerTests_test_disabled_by_default

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'import faulthandler; print(faulthandler.is_enabled())'
    args = (sys.executable, '-E', '-c', code)
    output = subprocess.check_output(args)
    self.assertEqual(output.rstrip(), b'False')
