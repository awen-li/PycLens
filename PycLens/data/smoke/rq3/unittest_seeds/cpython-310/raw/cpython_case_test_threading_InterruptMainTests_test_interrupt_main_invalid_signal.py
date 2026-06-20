# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: InterruptMainTests_test_interrupt_main_invalid_signal

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(ValueError, _thread.interrupt_main, -1)
    self.assertRaises(ValueError, _thread.interrupt_main, signal.NSIG)
    self.assertRaises(ValueError, _thread.interrupt_main, 1000000)
