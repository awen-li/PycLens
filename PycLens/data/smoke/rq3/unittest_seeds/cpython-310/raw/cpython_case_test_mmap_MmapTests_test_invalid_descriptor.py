# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mmap.py
# case: MmapTests_test_invalid_descriptor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = socket.socket()
    try:
        with self.assertRaises(OSError):
            m = mmap.mmap(s.fileno(), 10)
    finally:
        s.close()
