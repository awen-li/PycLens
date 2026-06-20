# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__osx_support.py
# case: Test_OSXSupport_test__find_appropriate_compiler

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    compilers = (('gcc-test', 'i686-apple-darwin11-llvm-gcc-4.2'), ('clang', 'clang version 3.1'))
    config_vars = {'CC': 'gcc-test -pthreads', 'CXX': 'cc++-test', 'CFLAGS': '-fno-strict-aliasing  -g -O3 -arch ppc -arch i386  ', 'LDFLAGS': '-arch ppc -arch i386   -g', 'CPPFLAGS': '-I. -isysroot /Developer/SDKs/MacOSX10.4u.sdk', 'BLDSHARED': 'gcc-test -bundle -arch ppc -arch i386 -g', 'LDSHARED': 'gcc-test -bundle -arch ppc -arch i386 -isysroot /Developer/SDKs/MacOSX10.4u.sdk -g'}
    expected_vars = {'CC': 'clang -pthreads', 'CXX': 'clang++', 'CFLAGS': '-fno-strict-aliasing  -g -O3 -arch ppc -arch i386  ', 'LDFLAGS': '-arch ppc -arch i386   -g', 'CPPFLAGS': '-I. -isysroot /Developer/SDKs/MacOSX10.4u.sdk', 'BLDSHARED': 'clang -bundle -arch ppc -arch i386 -g', 'LDSHARED': 'clang -bundle -arch ppc -arch i386 -isysroot /Developer/SDKs/MacOSX10.4u.sdk -g'}
    self.add_expected_saved_initial_values(config_vars, expected_vars)
    suffix = ':' + self.env['PATH'] if self.env['PATH'] else ''
    self.env['PATH'] = os.path.abspath(self.temp_path_dir) + suffix
    for (c_name, c_output) in compilers:
        os_helper.unlink(c_name)
        self.addCleanup(os_helper.unlink, c_name)
        with open(c_name, 'w') as f:
            f.write('#!/bin/sh\n/bin/echo ' + c_output)
        os.chmod(c_name, stat.S_IRWXU)
    self.assertEqual(expected_vars, _osx_support._find_appropriate_compiler(config_vars))
