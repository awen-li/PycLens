# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_file_eintr.py
# case: TestBufferedIOSignalInterrupt_test_readall

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._test_reading(data_to_write=b'hello\nworld!', read_and_verify_code=self._READING_CODE_TEMPLATE.format(read_method_name='read', expected=b'hello\nworld!\n'))
