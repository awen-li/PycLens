# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: MiscReadTestBase_test_check_members

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for tarinfo in self.tar:
        self.assertEqual(int(tarinfo.mtime), 1041808783, 'wrong mtime for %s' % tarinfo.name)
        if not tarinfo.name.startswith('ustar/'):
            continue
        self.assertEqual(tarinfo.uname, 'tarfile', 'wrong uname for %s' % tarinfo.name)
