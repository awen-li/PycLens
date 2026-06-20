# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_seek_with_encoder_state

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = self.open(os_helper.TESTFN, 'w', encoding='euc_jis_2004')
    f.write('æ̀')
    p0 = f.tell()
    f.write('æ')
    f.seek(p0)
    f.write('̀')
    f.close()
    f = self.open(os_helper.TESTFN, 'r', encoding='euc_jis_2004')
    self.assertEqual(f.readline(), 'æ̀̀')
    f.close()
