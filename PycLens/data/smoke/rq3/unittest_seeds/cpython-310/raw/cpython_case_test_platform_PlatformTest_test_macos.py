# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_platform.py
# case: PlatformTest_test_macos

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.addCleanup(self.clear_caches)
    uname = ('Darwin', 'hostname', '17.7.0', 'Darwin Kernel Version 17.7.0: Thu Jun 21 22:53:14 PDT 2018; root:xnu-4570.71.2~1/RELEASE_X86_64', 'x86_64', 'i386')
    arch = ('64bit', '')
    with mock.patch.object(platform, 'uname', return_value=uname), mock.patch.object(platform, 'architecture', return_value=arch):
        for (mac_ver, expected_terse, expected) in [(('', '', ''), 'Darwin-17.7.0', 'Darwin-17.7.0-x86_64-i386-64bit'), (('10.13.6', ('', '', ''), 'x86_64'), 'macOS-10.13.6', 'macOS-10.13.6-x86_64-i386-64bit')]:
            with mock.patch.object(platform, 'mac_ver', return_value=mac_ver):
                self.clear_caches()
                self.assertEqual(platform.platform(terse=1), expected_terse)
                self.assertEqual(platform.platform(), expected)
