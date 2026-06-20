# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BytesTest_test_buffer_is_readonly

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fd = os.open(__file__, os.O_RDONLY)
    with open(fd, 'rb', buffering=0) as f:
        self.assertRaises(TypeError, f.readinto, b'')
