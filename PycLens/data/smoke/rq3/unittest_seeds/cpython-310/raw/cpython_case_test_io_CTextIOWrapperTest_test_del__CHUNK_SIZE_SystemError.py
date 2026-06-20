# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: CTextIOWrapperTest_test_del__CHUNK_SIZE_SystemError

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t = self.TextIOWrapper(self.BytesIO(), encoding='ascii')
    with self.assertRaises(AttributeError):
        del t._CHUNK_SIZE
