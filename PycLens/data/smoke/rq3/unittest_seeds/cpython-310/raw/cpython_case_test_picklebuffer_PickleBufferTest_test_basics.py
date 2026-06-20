# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_picklebuffer.py
# case: PickleBufferTest_test_basics

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pb = PickleBuffer(b'foo')
    self.assertEqual(b'foo', bytes(pb))
    with memoryview(pb) as m:
        self.assertTrue(m.readonly)
    pb = PickleBuffer(bytearray(b'foo'))
    self.assertEqual(b'foo', bytes(pb))
    with memoryview(pb) as m:
        self.assertFalse(m.readonly)
        m[0] = 48
    self.assertEqual(b'0oo', bytes(pb))
