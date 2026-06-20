# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: Win32SymlinkTests_test_appexeclink

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    root = os.path.expandvars('%LOCALAPPDATA%\\Microsoft\\WindowsApps')
    if not os.path.isdir(root):
        self.skipTest('test requires a WindowsApps directory')
    aliases = [os.path.join(root, a) for a in fnmatch.filter(os.listdir(root), '*.exe')]
    for alias in aliases:
        if support.verbose:
            print()
            print('Testing with', alias)
        st = os.lstat(alias)
        self.assertEqual(st, os.stat(alias))
        self.assertFalse(stat.S_ISLNK(st.st_mode))
        self.assertEqual(st.st_reparse_tag, stat.IO_REPARSE_TAG_APPEXECLINK)
        break
    else:
        self.skipTest('test requires an app execution alias')
