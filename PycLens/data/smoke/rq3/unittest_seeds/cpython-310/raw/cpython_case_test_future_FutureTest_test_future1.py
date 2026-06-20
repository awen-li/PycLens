# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_future.py
# case: FutureTest_test_future1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with import_helper.CleanImport('future_test1'):
        from test import future_test1
        self.assertEqual(future_test1.result, 6)
