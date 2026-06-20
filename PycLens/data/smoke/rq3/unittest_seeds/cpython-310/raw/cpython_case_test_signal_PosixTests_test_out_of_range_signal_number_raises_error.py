# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_signal.py
# case: PosixTests_test_out_of_range_signal_number_raises_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(ValueError, signal.getsignal, 4242)
    self.assertRaises(ValueError, signal.signal, 4242, self.trivial_signal_handler)
    self.assertRaises(ValueError, signal.strsignal, 4242)
