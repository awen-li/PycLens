# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: ChannelIDTests_test_equality

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cid1 = interpreters.channel_create()
    cid2 = interpreters._channel_id(int(cid1))
    cid3 = interpreters.channel_create()
    self.assertTrue(cid1 == cid1)
    self.assertTrue(cid1 == cid2)
    self.assertTrue(cid1 == int(cid1))
    self.assertTrue(int(cid1) == cid1)
    self.assertTrue(cid1 == float(int(cid1)))
    self.assertTrue(float(int(cid1)) == cid1)
    self.assertFalse(cid1 == float(int(cid1)) + 0.1)
    self.assertFalse(cid1 == str(int(cid1)))
    self.assertFalse(cid1 == 2 ** 1000)
    self.assertFalse(cid1 == float('inf'))
    self.assertFalse(cid1 == 'spam')
    self.assertFalse(cid1 == cid3)
    self.assertFalse(cid1 != cid1)
    self.assertFalse(cid1 != cid2)
    self.assertTrue(cid1 != cid3)
