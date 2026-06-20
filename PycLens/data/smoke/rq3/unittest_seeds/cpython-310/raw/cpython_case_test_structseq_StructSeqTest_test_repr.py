# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_structseq.py
# case: StructSeqTest_test_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t = time.gmtime()
    self.assertTrue(repr(t))
    t = time.gmtime(0)
    self.assertEqual(repr(t), 'time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)')
    st = os.stat(__file__)
    rep = repr(st)
    self.assertTrue(rep.startswith('os.stat_result'))
    self.assertIn('st_mode=', rep)
    self.assertIn('st_ino=', rep)
    self.assertIn('st_dev=', rep)
