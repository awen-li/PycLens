# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_platform.py
# case: PlatformTest_test_parse_os_release

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    info = platform._parse_os_release(FEDORA_OS_RELEASE.splitlines())
    self.assertEqual(info['NAME'], 'Fedora')
    self.assertEqual(info['ID'], 'fedora')
    self.assertNotIn('ID_LIKE', info)
    self.assertEqual(info['VERSION_CODENAME'], '')
    info = platform._parse_os_release(UBUNTU_OS_RELEASE.splitlines())
    self.assertEqual(info['NAME'], 'Ubuntu')
    self.assertEqual(info['ID'], 'ubuntu')
    self.assertEqual(info['ID_LIKE'], 'debian')
    self.assertEqual(info['VERSION_CODENAME'], 'focal')
    info = platform._parse_os_release(TEST_OS_RELEASE.splitlines())
    expected = {'ID': 'linux', 'NAME': 'Linux', 'PRETTY_NAME': 'Linux', 'ID_LIKE': 'egg spam viking', 'EMPTY': '', 'DOUBLE_QUOTE': 'double', 'EMPTY_DOUBLE': '', 'SINGLE_QUOTE': 'single', 'EMPTY_SINGLE': '', 'QUOTES': "double's", 'SPECIALS': '$`\\\'"'}
    self.assertEqual(info, expected)
    self.assertEqual(len(info['SPECIALS']), 5)
