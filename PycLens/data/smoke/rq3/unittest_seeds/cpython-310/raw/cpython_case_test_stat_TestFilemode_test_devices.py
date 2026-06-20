# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_stat.py
# case: TestFilemode_test_devices

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if os.path.exists(os.devnull):
        (st_mode, modestr) = self.get_mode(os.devnull, lstat=False)
        self.assertEqual(modestr[0], 'c')
        self.assertS_IS('CHR', st_mode)
    for blockdev in ('/dev/sda', '/dev/hda'):
        if os.path.exists(blockdev):
            (st_mode, modestr) = self.get_mode(blockdev, lstat=False)
            self.assertEqual(modestr[0], 'b')
            self.assertS_IS('BLK', st_mode)
            break
