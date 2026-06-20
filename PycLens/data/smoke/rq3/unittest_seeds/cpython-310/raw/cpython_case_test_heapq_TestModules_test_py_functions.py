# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_heapq.py
# case: TestModules_test_py_functions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for fname in func_names:
        self.assertEqual(getattr(py_heapq, fname).__module__, 'heapq')
