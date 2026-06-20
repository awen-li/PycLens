# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_picklebuffer.py
# case: PickleBufferTest_test_raw_non_contiguous

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ndarray = import_helper.import_module('_testbuffer').ndarray
    arr = ndarray(list(range(6)), shape=(6,), format='<i')[::2]
    self.check_raw_non_contiguous(arr)
    arr = ndarray(list(range(12)), shape=(4, 3), format='<i')[::2]
    self.check_raw_non_contiguous(arr)
