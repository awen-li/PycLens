# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: ShareableTypeTests_test_singletons

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for obj in [None]:
        with self.subTest(obj):
            interpreters.channel_send(self.cid, obj)
            got = interpreters.channel_recv(self.cid)
            self.assertIs(got, obj)
