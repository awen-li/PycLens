# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__osx_support.py
# case: Test_OSXSupport_test__find_build_tool

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    out = _osx_support._find_build_tool('cc')
    self.assertTrue(os.path.isfile(out), 'cc not found - check xcode-select')
