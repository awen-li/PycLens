# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_picklebuffer.py
# case: PickleBufferTest_test_raw_ndarray

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ndarray = import_helper.import_module('_testbuffer').ndarray
    arr = ndarray(list(range(3)), shape=(3,), format='<h')
    equiv = b'\x00\x00\x01\x00\x02\x00'
    self.check_raw(arr, equiv)
    arr = ndarray(list(range(6)), shape=(2, 3), format='<h')
    equiv = b'\x00\x00\x01\x00\x02\x00\x03\x00\x04\x00\x05\x00'
    self.check_raw(arr, equiv)
    arr = ndarray(list(range(6)), shape=(2, 3), strides=(2, 4), format='<h')
    equiv = b'\x00\x00\x01\x00\x02\x00\x03\x00\x04\x00\x05\x00'
    self.check_raw(arr, equiv)
    arr = ndarray(456, shape=(), format='<i')
    equiv = b'\xc8\x01\x00\x00'
    self.check_raw(arr, equiv)
