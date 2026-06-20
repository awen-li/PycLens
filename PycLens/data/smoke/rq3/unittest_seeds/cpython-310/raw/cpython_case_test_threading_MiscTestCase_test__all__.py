# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: MiscTestCase_test__all__

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    restore_default_excepthook(self)
    extra = {'ThreadError'}
    not_exported = {'currentThread', 'activeCount'}
    support.check__all__(self, threading, ('threading', '_thread'), extra=extra, not_exported=not_exported)
