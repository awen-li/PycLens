# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: ThreadingTest_test_threading

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    DefaultContext = self.decimal.DefaultContext
    if self.decimal == C and (not self.decimal.HAVE_THREADS):
        self.skipTest('compiled without threading')
    save_prec = DefaultContext.prec
    save_emax = DefaultContext.Emax
    save_emin = DefaultContext.Emin
    DefaultContext.prec = 24
    DefaultContext.Emax = 425000000
    DefaultContext.Emin = -425000000
    self.synchro = threading.Event()
    self.finish1 = threading.Event()
    self.finish2 = threading.Event()
    th1 = threading.Thread(target=thfunc1, args=(self,))
    th2 = threading.Thread(target=thfunc2, args=(self,))
    th1.start()
    th2.start()
    self.finish1.wait()
    self.finish2.wait()
    for sig in Signals[self.decimal]:
        self.assertFalse(DefaultContext.flags[sig])
    th1.join()
    th2.join()
    DefaultContext.prec = save_prec
    DefaultContext.Emax = save_emax
    DefaultContext.Emin = save_emin
