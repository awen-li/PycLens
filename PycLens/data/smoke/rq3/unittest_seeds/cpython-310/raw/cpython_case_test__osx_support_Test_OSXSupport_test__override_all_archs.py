# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__osx_support.py
# case: Test_OSXSupport_test__override_all_archs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.env['ARCHFLAGS'] = '-arch x86_64'
    config_vars = {'CC': 'clang', 'CFLAGS': '-fno-strict-aliasing  -g -O3 -arch ppc -arch i386  ', 'LDFLAGS': '-arch ppc -arch i386   -g', 'CPPFLAGS': '-I. -isysroot /Developer/SDKs/MacOSX10.4u.sdk', 'BLDSHARED': 'gcc-4.0 -bundle  -arch ppc -arch i386 -g', 'LDSHARED': 'gcc-4.0 -bundle -arch ppc -arch i386 -isysroot /Developer/SDKs/MacOSX10.4u.sdk -g'}
    expected_vars = {'CC': 'clang', 'CFLAGS': '-fno-strict-aliasing  -g -O3     -arch x86_64', 'LDFLAGS': '    -g -arch x86_64', 'CPPFLAGS': '-I. -isysroot /Developer/SDKs/MacOSX10.4u.sdk', 'BLDSHARED': 'gcc-4.0 -bundle    -g -arch x86_64', 'LDSHARED': 'gcc-4.0 -bundle   -isysroot /Developer/SDKs/MacOSX10.4u.sdk -g -arch x86_64'}
    self.add_expected_saved_initial_values(config_vars, expected_vars)
    self.assertEqual(expected_vars, _osx_support._override_all_archs(config_vars))
