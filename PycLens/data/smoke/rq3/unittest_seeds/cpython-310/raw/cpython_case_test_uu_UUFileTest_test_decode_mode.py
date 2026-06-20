# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_uu.py
# case: UUFileTest_test_decode_mode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected_mode = 292
    with open(self.tmpin, 'wb') as f:
        f.write(encodedtextwrapped(expected_mode, self.tmpout))
    self.addCleanup(os.chmod, self.tmpout, expected_mode | stat.S_IWRITE)
    with open(self.tmpin, 'rb') as f:
        uu.decode(f)
    self.assertEqual(stat.S_IMODE(os.stat(self.tmpout).st_mode), expected_mode)
