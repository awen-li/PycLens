# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_file_eintr.py
# case: TestFileIOSignalInterrupt_test_readline

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._test_reading(data_to_write=b'hello, world!', read_and_verify_code=self._READING_CODE_TEMPLATE.format(read_method_name='readline', expected=b'hello, world!\n'))
