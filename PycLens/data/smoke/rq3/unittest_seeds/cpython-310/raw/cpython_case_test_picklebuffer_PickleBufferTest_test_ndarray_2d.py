# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_picklebuffer.py
# case: PickleBufferTest_test_ndarray_2d

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ndarray = import_helper.import_module('_testbuffer').ndarray
    arr = ndarray(list(range(12)), shape=(4, 3), format='<i')
    self.assertTrue(arr.c_contiguous)
    self.assertFalse(arr.f_contiguous)
    pb = PickleBuffer(arr)
    self.check_memoryview(pb, arr)
    arr = arr[::2]
    self.assertFalse(arr.c_contiguous)
    self.assertFalse(arr.f_contiguous)
    pb = PickleBuffer(arr)
    self.check_memoryview(pb, arr)
    arr = ndarray(list(range(12)), shape=(3, 4), strides=(4, 12), format='<i')
    self.assertTrue(arr.f_contiguous)
    self.assertFalse(arr.c_contiguous)
    pb = PickleBuffer(arr)
    self.check_memoryview(pb, arr)
