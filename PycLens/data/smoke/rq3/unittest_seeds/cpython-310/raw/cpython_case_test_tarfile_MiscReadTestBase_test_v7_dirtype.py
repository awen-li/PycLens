# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: MiscReadTestBase_test_v7_dirtype

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tarinfo = self.tar.getmember('misc/dirtype-old-v7')
    self.assertEqual(tarinfo.type, tarfile.DIRTYPE, 'v7 dirtype failed')
