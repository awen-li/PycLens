# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: GNUWriteTest_test_longnamelink_1024

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._test('longnam/' * 127 + 'longname', 'longlnk/' * 127 + 'longlink')
