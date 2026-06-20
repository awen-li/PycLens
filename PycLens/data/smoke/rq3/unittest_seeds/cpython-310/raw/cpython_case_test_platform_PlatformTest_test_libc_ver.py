# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_platform.py
# case: PlatformTest_test_libc_ver

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if os.path.isdir(sys.executable) and os.path.exists(sys.executable + '.exe'):
        executable = sys.executable + '.exe'
    elif sys.platform == 'win32' and (not os.path.exists(sys.executable)):
        import _winapi
        executable = _winapi.GetModuleFileName(0)
    else:
        executable = sys.executable
    platform.libc_ver(executable)
    filename = os_helper.TESTFN
    self.addCleanup(os_helper.unlink, filename)
    with mock.patch('os.confstr', create=True, return_value='mock 1.0'):
        self.assertEqual(platform.libc_ver(), ('mock', '1.0'))
        for (data, expected) in ((b'__libc_init', ('libc', '')), (b'GLIBC_2.9', ('glibc', '2.9')), (b'libc.so.1.2.5', ('libc', '1.2.5')), (b'libc_pthread.so.1.2.5', ('libc', '1.2.5_pthread')), (b'', ('', ''))):
            with open(filename, 'wb') as fp:
                fp.write(b'[xxx%sxxx]' % data)
                fp.flush()
            self.assertEqual(platform.libc_ver(executable=filename), expected)
    chunksize = 16384
    with open(filename, 'wb') as f:
        f.write(b'x' * (chunksize - 10))
        f.write(b'GLIBC_1.23.4\x00GLIBC_1.9\x00GLIBC_1.21\x00')
    self.assertEqual(platform.libc_ver(filename, chunksize=chunksize), ('glibc', '1.23.4'))
