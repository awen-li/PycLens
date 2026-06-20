# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakset.py
# case: TestWeakSet_test_methods

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    weaksetmethods = dir(WeakSet)
    for method in dir(set):
        if method == 'test_c_api' or method.startswith('_'):
            continue
        self.assertIn(method, weaksetmethods, 'WeakSet missing method ' + method)
