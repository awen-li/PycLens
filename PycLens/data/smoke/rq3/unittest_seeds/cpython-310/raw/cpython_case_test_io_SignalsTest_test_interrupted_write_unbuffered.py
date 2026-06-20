# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: SignalsTest_test_interrupted_write_unbuffered

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_interrupted_write(b'xy', b'xy', mode='wb', buffering=0)
