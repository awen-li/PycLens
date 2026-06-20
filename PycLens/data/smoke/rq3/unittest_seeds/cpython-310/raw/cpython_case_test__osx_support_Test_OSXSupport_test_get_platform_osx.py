# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__osx_support.py
# case: Test_OSXSupport_test_get_platform_osx

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    config_vars = {'CFLAGS': '-fno-strict-aliasing  -g -O3 -arch ppc -arch i386  -isysroot /Developer/SDKs/MacOSX10.1.sdk', 'MACOSX_DEPLOYMENT_TARGET': '10.6'}
    result = _osx_support.get_platform_osx(config_vars, ' ', ' ', ' ')
    self.assertEqual(('macosx', '10.6', 'fat'), result)
