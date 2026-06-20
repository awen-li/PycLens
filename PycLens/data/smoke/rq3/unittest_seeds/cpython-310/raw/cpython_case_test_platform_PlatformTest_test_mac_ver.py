# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_platform.py
# case: PlatformTest_test_mac_ver

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    res = platform.mac_ver()
    if platform.uname().system == 'Darwin':
        output = subprocess.check_output(['sw_vers'], text=True)
        for line in output.splitlines():
            if line.startswith('ProductVersion:'):
                real_ver = line.strip().split()[-1]
                break
        else:
            self.fail(f'failed to parse sw_vers output: {output!r}')
        result_list = res[0].split('.')
        expect_list = real_ver.split('.')
        len_diff = len(result_list) - len(expect_list)
        if len_diff > 0:
            expect_list.extend(['0'] * len_diff)
        if result_list != ['10', '16']:
            self.assertEqual(result_list, expect_list)
        self.assertEqual(res[1], ('', '', ''))
        if sys.byteorder == 'little':
            self.assertIn(res[2], ('i386', 'x86_64', 'arm64'))
        else:
            self.assertEqual(res[2], 'PowerPC')
