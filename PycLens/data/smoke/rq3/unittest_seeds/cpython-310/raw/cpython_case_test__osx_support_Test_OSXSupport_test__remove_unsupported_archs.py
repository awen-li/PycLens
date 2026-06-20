# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__osx_support.py
# case: Test_OSXSupport_test__remove_unsupported_archs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    config_vars = {'CC': 'clang', 'CFLAGS': '-fno-strict-aliasing  -g -O3 -arch ppc -arch i386  ', 'LDFLAGS': '-arch ppc -arch i386   -g', 'CPPFLAGS': '-I. -isysroot /Developer/SDKs/MacOSX10.4u.sdk', 'BLDSHARED': 'gcc-4.0 -bundle  -arch ppc -arch i386 -g', 'LDSHARED': 'gcc-4.0 -bundle  -arch ppc -arch i386 -isysroot /Developer/SDKs/MacOSX10.4u.sdk -g'}
    expected_vars = {'CC': 'clang', 'CFLAGS': '-fno-strict-aliasing  -g -O3  -arch i386  ', 'LDFLAGS': ' -arch i386   -g', 'CPPFLAGS': '-I. -isysroot /Developer/SDKs/MacOSX10.4u.sdk', 'BLDSHARED': 'gcc-4.0 -bundle   -arch i386 -g', 'LDSHARED': 'gcc-4.0 -bundle   -arch i386 -isysroot /Developer/SDKs/MacOSX10.4u.sdk -g'}
    self.add_expected_saved_initial_values(config_vars, expected_vars)
    suffix = ':' + self.env['PATH'] if self.env['PATH'] else ''
    self.env['PATH'] = os.path.abspath(self.temp_path_dir) + suffix
    c_name = 'clang'
    os_helper.unlink(c_name)
    self.addCleanup(os_helper.unlink, c_name)
    with open(c_name, 'w') as f:
        f.write('#!/bin/sh\nexit 255')
    os.chmod(c_name, stat.S_IRWXU)
    self.assertEqual(expected_vars, _osx_support._remove_unsupported_archs(config_vars))
