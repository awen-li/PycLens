# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_multibyte_seek_and_tell

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = self.open(os_helper.TESTFN, 'w', encoding='euc_jp')
    f.write('AB\nうえ\n')
    f.close()
    f = self.open(os_helper.TESTFN, 'r', encoding='euc_jp')
    self.assertEqual(f.readline(), 'AB\n')
    p0 = f.tell()
    self.assertEqual(f.readline(), 'うえ\n')
    p1 = f.tell()
    f.seek(p0)
    self.assertEqual(f.readline(), 'うえ\n')
    self.assertEqual(f.tell(), p1)
    f.close()
