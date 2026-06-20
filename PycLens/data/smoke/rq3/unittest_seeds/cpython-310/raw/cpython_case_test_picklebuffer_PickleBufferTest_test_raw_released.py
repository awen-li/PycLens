# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_picklebuffer.py
# case: PickleBufferTest_test_raw_released

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pb = PickleBuffer(b'foo')
    pb.release()
    with self.assertRaises(ValueError) as raises:
        pb.raw()
