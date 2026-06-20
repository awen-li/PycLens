# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: MemberReadTest_test_find_regtype_oldv7

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tarinfo = self.tar.getmember('misc/regtype-old-v7')
    self._test_member(tarinfo, size=7011, chksum=sha256_regtype)
