# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: MemberReadTest_test_find_dirtype_with_size

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tarinfo = self.tar.getmember('ustar/dirtype-with-size')
    self._test_member(tarinfo, size=255)
