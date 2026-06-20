# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_pybuffer_size_from_format

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for format in ('', 'ii', '3s'):
        self.assertEqual(_testcapi.PyBuffer_SizeFromFormat(format), struct.calcsize(format))
