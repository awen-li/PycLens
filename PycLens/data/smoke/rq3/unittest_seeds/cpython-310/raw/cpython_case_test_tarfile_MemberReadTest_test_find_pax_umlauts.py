# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: MemberReadTest_test_find_pax_umlauts

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.tar.close()
    self.tar = tarfile.open(self.tarname, mode=self.mode, encoding='iso8859-1')
    tarinfo = self.tar.getmember('pax/umlauts-ÄÖÜäöüß')
    self._test_member(tarinfo, size=7011, chksum=sha256_regtype)
