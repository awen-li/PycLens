# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_platform.py
# case: PlatformTest_test_freedesktop_os_release

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.addCleanup(self.clear_caches)
    self.clear_caches()
    if any((os.path.isfile(fn) for fn in platform._os_release_candidates)):
        info = platform.freedesktop_os_release()
        self.assertIn('NAME', info)
        self.assertIn('ID', info)
        info['CPYTHON_TEST'] = 'test'
        self.assertNotIn('CPYTHON_TEST', platform.freedesktop_os_release())
    else:
        with self.assertRaises(OSError):
            platform.freedesktop_os_release()
