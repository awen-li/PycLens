# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_signal.py
# case: RaiseSignalTest_test_invalid_argument

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        SIGHUP = 1
        signal.raise_signal(SIGHUP)
        self.fail('OSError (Invalid argument) expected')
    except OSError as e:
        if e.errno == errno.EINVAL:
            pass
        else:
            raise
