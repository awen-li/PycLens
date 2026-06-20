# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: BaseTest_test_obsolete_write_lock

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from _testcapi import getbuffer_with_null_view
    a = array.array('B', b'')
    self.assertRaises(BufferError, getbuffer_with_null_view, a)
