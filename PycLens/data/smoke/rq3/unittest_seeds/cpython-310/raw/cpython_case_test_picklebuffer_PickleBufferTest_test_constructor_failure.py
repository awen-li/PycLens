# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_picklebuffer.py
# case: PickleBufferTest_test_constructor_failure

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError):
        PickleBuffer()
    with self.assertRaises(TypeError):
        PickleBuffer('foo')
    m = memoryview(b'foo')
    m.release()
    with self.assertRaises(ValueError):
        PickleBuffer(m)
