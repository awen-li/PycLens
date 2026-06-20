# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: HardlinkTest_test_add_twice

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tarinfo = self.tar.gettarinfo(self.foo)
    self.assertEqual(tarinfo.type, tarfile.REGTYPE, 'add file as regular failed')
