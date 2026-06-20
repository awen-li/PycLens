# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_future.py
# case: FutureTest_test_unicode_literals_exec

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    scope = {}
    exec("from __future__ import unicode_literals; x = ''", {}, scope)
    self.assertIsInstance(scope['x'], str)
