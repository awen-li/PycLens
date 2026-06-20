# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_stat.py
# case: TestFilemode_test_mode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(TESTFN, 'w'):
        pass
    if os.name == 'posix':
        os.chmod(TESTFN, 448)
        (st_mode, modestr) = self.get_mode()
        self.assertEqual(modestr, '-rwx------')
        self.assertS_IS('REG', st_mode)
        self.assertEqual(self.statmod.S_IMODE(st_mode), self.statmod.S_IRWXU)
        os.chmod(TESTFN, 56)
        (st_mode, modestr) = self.get_mode()
        self.assertEqual(modestr, '----rwx---')
        self.assertS_IS('REG', st_mode)
        self.assertEqual(self.statmod.S_IMODE(st_mode), self.statmod.S_IRWXG)
        os.chmod(TESTFN, 7)
        (st_mode, modestr) = self.get_mode()
        self.assertEqual(modestr, '-------rwx')
        self.assertS_IS('REG', st_mode)
        self.assertEqual(self.statmod.S_IMODE(st_mode), self.statmod.S_IRWXO)
        os.chmod(TESTFN, 292)
        (st_mode, modestr) = self.get_mode()
        self.assertS_IS('REG', st_mode)
        self.assertEqual(modestr, '-r--r--r--')
        self.assertEqual(self.statmod.S_IMODE(st_mode), 292)
    else:
        os.chmod(TESTFN, 448)
        (st_mode, modestr) = self.get_mode()
        self.assertEqual(modestr[:3], '-rw')
        self.assertS_IS('REG', st_mode)
        self.assertEqual(self.statmod.S_IFMT(st_mode), self.statmod.S_IFREG)
