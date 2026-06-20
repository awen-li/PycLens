# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncore.py
# case: DispatcherTests_test_basic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = asyncore.dispatcher()
    self.assertEqual(d.readable(), True)
    self.assertEqual(d.writable(), True)
