# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__osx_support.py
# case: Test_OSXSupport_test__remove_universal_flags

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    config_vars = {'CFLAGS': '-fno-strict-aliasing  -g -O3 -arch ppc -arch i386  ', 'LDFLAGS': '-arch ppc -arch i386   -g', 'CPPFLAGS': '-I. -isysroot /Developer/SDKs/MacOSX10.4u.sdk', 'BLDSHARED': 'gcc-4.0 -bundle  -arch ppc -arch i386 -g', 'LDSHARED': 'gcc-4.0 -bundle  -arch ppc -arch i386 -isysroot /Developer/SDKs/MacOSX10.4u.sdk -g'}
    expected_vars = {'CFLAGS': '-fno-strict-aliasing  -g -O3    ', 'LDFLAGS': '    -g', 'CPPFLAGS': '-I.  ', 'BLDSHARED': 'gcc-4.0 -bundle    -g', 'LDSHARED': 'gcc-4.0 -bundle      -g'}
    self.add_expected_saved_initial_values(config_vars, expected_vars)
    self.assertEqual(expected_vars, _osx_support._remove_universal_flags(config_vars))
